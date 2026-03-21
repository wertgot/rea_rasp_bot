with open('database/teachers.txt', 'r', encoding='utf-8') as f:
    teachers = eval(f.read())
print(len(teachers))

tt = []
for t in teachers:
    if '/' not in t:
        tt.append(t)
print(len(tt))
