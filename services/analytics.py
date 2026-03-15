def vacant_rooms(pair_num, corpus) -> list[str]:
    """свободные аудитории по номеру пары и корпуса"""

    with open('database/today_pairs.txt', 'r', encoding='utf-8') as f:
        today_pairs = eval(f.read())

    with open('database/all_rooms.txt', 'r', encoding='utf-8') as f:
        all_rooms = eval(f.read())

    pairs = set()
    for pair in today_pairs:
        if pair[1] == pair_num and pair[2] == corpus:
            pairs.add(tuple(pair[-1]))

    rooms = set()
    for room in all_rooms:
        if room[0] == corpus:
            rooms.add(room[-1])

    print(len(pairs), len(rooms))

    v_rooms = list(rooms - pairs)
    v_rooms.sort(key=lambda x: x[-1])
    return v_rooms
