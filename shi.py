
with open('today_pairs_list_13.03.2026.txt', 'r') as f:
    pair_list = eval(f.read())
    print(len(pair_list))


all_classes = set()

for pair in pair_list:
    all_classes.add((pair[1:]))

with open('all_classes.txt', 'w') as f:
    f.write(str(all_classes))

'''
with open('today_pairs_list.txt', 'w', encoding='utf-8') as f:
    f.write(str(list(set(pair_list))))
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
