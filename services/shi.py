import ast
with open('database/teachers.txt', 'r', encoding='utf-8') as f:
    teachers = ast.literal_eval(f.read())
print(len(teachers), type(teachers))
