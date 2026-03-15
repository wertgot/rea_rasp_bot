import functools

def pairs_num_by_corpuses_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        p_by_c = func(*args, **kwargs)
        nice_p_by_c = ""
        for p_num in sorted(p_by_c):
            nice_p_by_c += f"пара {p_num}:\n"
            for c in sorted(p_by_c[p_num]):
                nice_p_by_c += f"    корп. {c}:  {p_by_c[p_num][c]}\n"
            nice_p_by_c += '\n'
        return nice_p_by_c
    return wrapper
