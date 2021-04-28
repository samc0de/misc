import functools


@functools.lru_cache()
def get_largest_subsequence(str1: str, str2: str) -> int:
    if not str1 or not str2:
        return 0
    if str1[-1] == str2[-1]:
        return get_largest_subsequence(str1[:-1], str2[:-1]) + 1
    return max(
        get_largest_subsequence(str1[:-1], str2),
        get_largest_subsequence(str1, str2[:-1]))
