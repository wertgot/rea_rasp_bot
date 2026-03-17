all_rooms_2: set[tuple[int, str]] = set()

for i in range(14, 18):
    with open(f"database/today_pairs_{i}.03.2026.txt", 'r') as f:
        pairs = eval(f.read())
    for pair in pairs:
        all_rooms_2.add(tuple(pair[2:]))

print('all_rooms_2', len(all_rooms_2))

with open("database/all_rooms.txt", 'r') as f:
    all_rooms = eval(f.read())

print('all_rooms', len(all_rooms))

ar = all_rooms | all_rooms_2

print(len(ar))

with open("database/all_rooms.txt", 'w') as f:
    f.write(str(ar))