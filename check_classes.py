import requests
from bs4 import BeautifulSoup
import re


def parse_classrooms(html_content):
    """Извлечь из страницы расписания пары на сегодня"""

    soup = BeautifulSoup(html_content, 'html.parser')

    classrooms = []
    
    today_table = soup.find('table', {'id': 'today'})

    if not today_table or today_table.find('h5', string=re.compile('Занятия отсутствуют')):
        return []
    
    # Ищем все строки с занятиями (не пустые)
    slots = today_table.find_all('tr', class_=lambda x: x and 'slot' in x and 'load-empty' not in x)
    
    for slot in slots:
        # Ищем ссылку с информацией о занятии
        time_td = slot.find('td', style="width: 84px")
        if time_td:
            time_text = time_td.get_text(separator='\n', strip=True)
        else:
            print('ссылка с информацией о занятии не найдена')
        # Парсим номер пары
        lines = time_text.split('\n')
        if lines:
            pair_number = lines[0].split()[0]
        else:
            print('номер пары не определен:', lines)
        
        link = slot.find('a', class_='task')
        if link:
            # Получаем текст ссылки
            text = link.get_text(separator='\n', strip=True)
            
            # Ищем корпус и кабинет с помощью регулярного выражения
            # Формат: "X корпус - YYY" или "X корпус - YYY, пл. Основная"
            match = re.search(r'(\d+)\s+корпус\s*-\s*(\d+)', text)
            if match:
                building = match.group(1)
                room = match.group(2)
                classrooms.append((
                    pair_number, # какая пара по счету
                    building,    # корпус
                    room,        # кабинет
                ))
            else:
                print("странный формат кабинета:", text)
    
    return classrooms


def get_today_teachers_rasp(teacher):
    """Получить сегодняшние пары преподавателя"""

    session = requests.Session()

    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
    })

    try:
        # Сначала заходим на главную страницу (чтобы получить cookies)
        main_response = session.get(
            'https://rasp.rea.ru/',
            verify=False,   # отключаем проверку SSL
            timeout=10
        )
        main_response.raise_for_status()

        # Затем делаем нужный запрос
        params = {
            'selection': teacher,
            'weekNum': '-1',
            'catfilter': '0'
        }

        response = session.get(
            'https://rasp.rea.ru/Schedule/ScheduleCard',
            params=params,
            headers={'X-Requested-With': 'XMLHttpRequest'},
            verify=False,  # отключаем проверку SSL
            timeout=10
        )

        if response.status_code == 200:
            html_content = response.text
            classrooms = parse_classrooms(html_content)
            return classrooms
        else:
            print(f'Ошибка: {response.status_code}')
        
    except requests.exceptions.SSLError as e:
        print(f"SSL ошибка при подключении: {e}")
        return []
    except requests.exceptions.ConnectionError as e:
        print(f"Ошибка соединения: {e}")
        return []
    except requests.exceptions.Timeout:
        print("Таймаут при подключении к серверу")
        return []
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return []


if __name__ == "__main__":
    rasp = get_today_teachers_rasp('15.27Д-ПИ03/24б')
    for pair in rasp:
        print(pair)
