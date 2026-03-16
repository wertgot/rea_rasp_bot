import utils.beautymaker


def vacant_rooms(pair_num, corpus) -> list[str]:
    """свободные аудитории по номеру пары и корпуса"""

    with open('database/today_pairs.txt', 'r', encoding='utf-8') as f:
        today_pairs = eval(f.read())

    with open('database/all_rooms.txt', 'r', encoding='utf-8') as f:
        all_rooms = eval(f.read())

    pairs = set()
    for pair in today_pairs:
        if pair[1] == pair_num and pair[2] == corpus:
            pairs.add(pair[-1])

    rooms = set()
    for room in all_rooms:
        if room[0] == corpus:
            rooms.add(room[-1])

    v_rooms = list(rooms - pairs)
    v_rooms.sort()

    return v_rooms


@utils.beautymaker.pairs_num_by_corpuses_decorator
def pairs_num_by_corpuses():
    with open('database/today_pairs.txt', 'r', encoding='utf-8') as f:
        today_pairs = eval(f.read())

    p_by_c = {}
    for pair in today_pairs:
        p_by_c[pair[1]] = p_by_c.get(pair[1], {})
        p_by_c[pair[1]][pair[2]] = p_by_c[pair[1]].get(pair[2], 0) + 1

    return p_by_c
