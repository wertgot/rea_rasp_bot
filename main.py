from check_classes import get_today_teachers_rasp


with open('teacher_list.txt', 'r', encoding='utf-8') as f:
    teacher_list = eval(f.read())

occupied_classes: list[tuple] = []

for teacher in teacher_list:
    teacher_rasp = get_today_teachers_rasp(teacher)
    occupied_classes += teacher_rasp
print("всего пар сегодня", len(occupied_classes))

with open('today_pairs_list.txt', 'w', encoding='utf-8') as f:
    f.write(occupied_classes)
