import functools


@functools.lru_cache()
def get_largest_substring(str1: str, str2: str, count: int=0) -> int:
    if not str1 or not str2:
        return count
    if str1[-1] == str2[-1]:
        count = get_largest_substring(str1[:-1], str2[:-1], count + 1)
    else:
        count = max(count, max(
        get_largest_substring(str1[:-1], str2, 0),
        get_largest_substring(str1, str2[:-1], 0)))
    return count
