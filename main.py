# main.py
from check_classes import get_today_teachers_rasp
from datetime import datetime


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
