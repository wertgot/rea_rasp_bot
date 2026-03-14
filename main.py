# main.py
from check_classes import get_today_teachers_rasp
from datetime import datetime
import time


# Засекаем начало выполнения
start_time = time.time()
start_datetime = datetime.now()

print(f"🚀 Запуск: {start_datetime.strftime('%H:%M:%S')}")
print("=" * 50)

with open('teacher_list.txt', 'r', encoding='utf-8') as f:
    teacher_list = eval(f.read())

occupied_classes = set()

for teacher in teacher_list:
    teacher_rasp = get_today_teachers_rasp(teacher)
    occupied_classes = occupied_classes.union(set(teacher_rasp))
occupied_classes = list(occupied_classes)
print("всего пар сегодня", len(occupied_classes))


today = datetime.now().strftime("%d.%m.%Y")
filename = f'today_pairs_list_{today}.txt'
with open(filename, 'w', encoding='utf-8') as f:
    f.write(str(occupied_classes))

with open('today_pairs_list.txt', 'w', encoding='utf-8') as f:
    f.write(str(occupied_classes))

# Вычисляем общее время
end_time = time.time()
end_datetime = datetime.now()
total_time = end_time - start_time
minutes = int(total_time // 60)
seconds = int(total_time % 60)

print("=" * 50)
print(f"🏁 Завершение: {end_datetime.strftime('%H:%M:%S')}")
print(f"⏱️ Общее время выполнения: {minutes} мин {seconds} сек ({total_time:.2f} сек)")