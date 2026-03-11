import requests
from bs4 import BeautifulSoup


def get_departments() -> list[str]:
    """Извлекает список кафедр"""

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        url="https://rasp.rea.ru/"
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверка на ошибки HTTP
        response.encoding = 'utf-8'

        soup = BeautifulSoup(response.text, 'html.parser')

        cathedra_select = soup.find('select', {'name': 'Cathedra'})

        if not cathedra_select:
            print("Не удалось найти список кафедр на странице.")
            return []

        departments = []
        options = cathedra_select.find_all('option')
        for option in options:
            value = option.get('value')
            # Пропускаем служебную опцию "-кафедра-"
            if value and value != 'na' and value.strip():
                # названия кафедр находятся в атрибуте value
                departments.append(value.lower())
        return departments  

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к сайту: {e}")
        return []
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []


def get_teachers_from_department(dep):
    """Извлекает список преподавателей кафедры"""

    url = "https://rasp.rea.ru/Schedule/ScheduleCard"

    params = {
        "selection": dep,
        "weekNum": "-1",
        "catfilter": "0"
    }

    headers = {
        "accept": "text/html, */*; q=0.01",
        "referer": "https://rasp.rea.ru/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "x-requested-with": "XMLHttpRequest"
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        html_content = response.text

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except UnicodeEncodeError as e:
        print(f"Encoding error: {e}")
    
    soup = BeautifulSoup(html_content, 'html.parser')

    # находим все ФИО преповавателей
    teachers = []
    for name_link in soup.select('td:nth-of-type(2) a.search-link'):
        teachers.append(name_link.text.strip().lower())
    
    return teachers


if __name__ == "__main__":
    deps = get_departments()
    teacher_list = set()
    for dep in deps:
        teachers = get_teachers_from_department(dep)
        for teacher in teachers:
            teacher_list.add(teacher)
    teacher_list = list(teacher_list)
    print(f"Всего прероподавателей: {len(teacher_list)}")

    with open("teacher_list.txt", 'w', encoding='utf-8') as f:
        f.write(str(teacher_list))
    print("список преподавателей обновлен")
