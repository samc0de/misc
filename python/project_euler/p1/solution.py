"""Problem statement:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def get_multiples(root_factors, limit):
    multiples = []
    for num in range(1, limit):
        for factor in root_factors:
            if num % factor == 0:
                multiples.append(num)
                break

    return multiples


def get_sum_of_devisors(root_factors, limit):
    return sum(get_multiples(root_factors, limit))
