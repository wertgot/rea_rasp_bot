
with open('today_pairs_list.txt', 'r', encoding='utf-8') as f:
    pair_list = eval(f.read())
    print('всего пар', len(pair_list))
    print(pair_list[:5])



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
