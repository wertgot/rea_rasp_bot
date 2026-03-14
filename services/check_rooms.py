import requests
from bs4 import BeautifulSoup
import re
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def parse_rooms(html_content, teacher) -> set[tuple]:
    """Извлечь из страницы расписания пары на сегодня"""

    soup = BeautifulSoup(html_content, 'html.parser')

    rooms: set[tuple] = set()

    today_table = soup.find('table', {'id': 'today'})
    if not today_table:
        print('no table')
        return set()

    is_empty = today_table.find('h5', string=re.compile('Занятия отсутствуют'))  # type: ignore
    if is_empty:
        return set()

    # Ищем все строки с занятиями (не пустые)
    slots = today_table.select('tr.slot:not(.load-empty)')

    for slot in slots:
        # Ищем ссылку с информацией о занятии
        time_td = slot.find('td', style="width: 84px")
        if time_td:
            time_text = time_td.get_text(separator='\n', strip=True)
        else:
            print('ссылка с информацией о занятии не найдена')
            continue
        # Парсим номер пары
        pair_number = "0"
        lines = time_text.split('\n')
        if lines:
            pair_number =lines[0].split()[0]
        else:
            print('номер пары не определен:', lines)

        link = slot.find('a', class_='task')
        if link:
            # Получаем текст ссылки
            text = link.get_text(separator='\n', strip=True)

            # Ищем корпус и кабинет с помощью регулярного выражения
            # Формат: "X корпус - YYY" или "X корпус - YYY, пл. Основная"
            match = re.search(r'(\d+)\s+корпус\s*-\s*([\d./]+)', text)
            if match:
                building = match.group(1)
                room = match.group(2)
                rooms.add((
                    teacher,
                    int(pair_number), # какая пара по счету
                    int(building),    # корпус
                    room,        # кабинет
                ))
            else:
                print("странный формат кабинета:", text)

    return rooms


def create_session_with_retries() -> requests.Session:
    """Создать сессию с повторными попытками при ошибках"""

    session = requests.Session()

    # Настройка повторных попыток
    retry_strategy = Retry(
        total=5,  # максимальное количество попыток
        backoff_factor=2,  # фактор задержки между попытками
        status_forcelist=[429, 500, 502, 503, 504],  # коды для повторных попыток
        allowed_methods=["HEAD", "GET", "OPTIONS"]  # методы для повторных попыток
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
    })

    return session


def get_today_teachers_schedule(teacher) -> set[tuple]:
    """Получить сегодняшние пары преподавателя"""

    session = create_session_with_retries()

    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
    })

    try:
        params = {
            'selection': teacher,
            'weekNum': '-1',
            'catfilter': '0'
        }

        response = session.get(
            'https://rasp.rea.ru/Schedule/ScheduleCard',
            params=params,
            headers={'X-Requested-With': 'XMLHttpRequest'},
            timeout=15
        )

        if response.status_code == 200:
            html_content = response.text
            if "не найдено результатов" in html_content:
                print("По запросу ", teacher, "не найдено результатов.")
                return set()
            else:
                rooms = parse_rooms(html_content, teacher)
                if rooms:
                    print("успех:", teacher)
                else:
                    print("пусто:", teacher)
                return rooms
        else:
            print(f'Ошибка: {response.status_code}')

    except requests.exceptions.SSLError as e:
        print(f"SSL ошибка при подключении: {e}")
    except requests.exceptions.ConnectionError as e:
        print(f"Ошибка соединения: {e}")
    except requests.exceptions.Timeout:
        print("Таймаут при подключении к серверу")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
    return set()


if __name__ == "__main__":
    rasp = get_today_teachers_schedule("15.27Д-ПИ03/24б".lower())
    for pair in rasp:
        print(pair)
