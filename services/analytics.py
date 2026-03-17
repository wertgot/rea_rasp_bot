import utils.beautymaker


def vacant_rooms(pair_num, corpus) -> tuple[list[str], int]:
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
    return v_rooms, len(rooms)


@utils.beautymaker.pairs_num_by_corpuses_decorator # -> str
def pairs_num_by_corpuses() -> tuple[dict[int, dict[int, int]], int, int]:
    with open('database/today_pairs.txt', 'r', encoding='utf-8') as f:
        today_pairs = eval(f.read())
    today_pairs = [x[1:] for x in today_pairs]
    today_pairs = set(today_pairs)

    p_by_c = {}
    p_by_pn = {}
    for pair in today_pairs:
        p_by_c[pair[0]] = p_by_c.get(pair[0], {})
        p_by_c[pair[0]][pair[1]] = p_by_c[pair[0]].get(pair[1], 0) + 1

        p_by_pn[pair[0]] = p_by_pn.get(pair[0], 0) + 1

    max_pairs_together = max(p_by_pn.values())

    return p_by_c, len(today_pairs), max_pairs_together
