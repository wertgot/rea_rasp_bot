
with open('today_pairs_list.txt', 'r', encoding='utf-8') as f:
    pair_list = eval(f.read())
    print('всего пар', len(pair_list))
    print(pair_list[:5])

with open('all_classes.txt', 'r', encoding='utf-8') as f:
    all_classes = eval(f.read())

def vacant_classes(all_classes, pair_list, pair_num, pair_corp):
    pairs = set()
    for pair in pair_list:
        if pair[1] == pair_num and pair[2] == pair_corp:
            pairs.add(tuple(pair[2:]))

    classes = set()
    for clas in all_classes:
        if clas[0] == pair_corp:
            classes.add(clas)
    
    v_cls = list(classes - pairs)
    v_cls.sort(key=lambda x: x[-1])
    return v_cls

rooms1 = vacant_classes(all_classes, pair_list, pair_num=2, pair_corp=3)
rooms2 = vacant_classes(all_classes, pair_list, pair_num=3, pair_corp=3)
for room in rooms1:
    if room in rooms2:
        print(room)

'''
all_classes_today = set()

for pair in pair_list:
    all_classes_today.add((pair[2:]))

with open('all_classes.txt', 'r') as f:
    all_classes = eval(f.read())

print(f'all_classes_today: {len(all_classes_today)}')
print(f'all_classes: {len(all_classes)}')

all_classes = all_classes.union(all_classes_today)

print(f'all_classes now: {len(all_classes)}')

with open('all_classes.txt', 'w') as f:
    f.write(str(all_classes))
'''


'''
pairs_together = {}

for pair in pair_list:
    pairs_together[pair[0]] = pairs_together.get(pair[0], [])
    pairs_together[pair[0]].append(pair)
'''

'''
for i in range(1, 9):
    now_p = pairs_together[i]
    corp_p = {}
    for p in now_p:
        corp_p[p[1]] = corp_p.get(p[1], [])
        corp_p[p[1]].append(p)
    print(i, ':')
    for c in [1, 2, 3, 4, 6, 8, 9]:
        print('   ', c, ':', len(corp_p.get(c, [])))
'''
