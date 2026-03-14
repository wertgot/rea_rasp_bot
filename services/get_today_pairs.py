from .check_rooms import get_today_teachers_schedule
from datetime import datetime
import time


def get_today_pairs():
    # Засекаем начало выполнения
    start_time = time.time()
    start_datetime = datetime.now()

    print(f"🚀 Запуск: {start_datetime.strftime('%H:%M:%S')}")
    print("=" * 50)

    with open("database/teachers.txt", 'r', encoding='utf-8') as f:
        teachers = eval(f.read())

    occupied_rooms = set()

    for teacher in teachers:
        teacher_rasp = get_today_teachers_schedule(teacher)
        occupied_rooms = occupied_rooms.union(set(teacher_rasp))
    occupied_rooms = list(occupied_rooms)
    print("всего пар сегодня", len(occupied_rooms))


    today = datetime.now().strftime("%d.%m.%Y")
    filename = f'database/today_pairs_{today}.txt'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(occupied_rooms))

    with open('database/today_pairs.txt', 'w', encoding='utf-8') as f:
        f.write(str(occupied_rooms))

    # Вычисляем общее время
    end_time = time.time()
    end_datetime = datetime.now()
    total_time = end_time - start_time
    minutes = int(total_time // 60)
    seconds = int(total_time % 60)

    print("=" * 50)
    print(f"🏁 Завершение: {end_datetime.strftime('%H:%M:%S')}")
    print(f"⏱️ Общее время выполнения: {minutes} мин {seconds} сек ({total_time:.2f} сек)")


if __name__ == "__main__":
    get_today_pairs()
