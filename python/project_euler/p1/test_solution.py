import pytest

import solution


def test_get_multiples__divisibility():
    """Test if the nums in the list returned are all divisible by 3 & 5."""
    roots = (3, 5)
    multiples = solution.get_multiples(root_factors=roots, limit=1000)
    # assert (all(not(x % f) for f in roots for x in multiples))
    assert (all(any(not(x % f) for f in roots) for x in multiples))


def test_get_multiples__non_empty():
    """Test if the nums in the list returned are all divisible by 3 & 5."""
    roots = (3, 5)
    multiples = solution.get_multiples(root_factors=roots, limit=1000)
    assert len(multiples)


def test_get_multiples__limit():
    """Test if the nums in the list returned are all divisible by 3 & 5."""
    roots = (3, 5)
    multiples = solution.get_multiples(root_factors=roots, limit=1000)
    assert (all(0 < x < 1000 for x in multiples))
