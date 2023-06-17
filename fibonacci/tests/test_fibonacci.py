import pytest
from fibonacci.naive import fibonacci_naive
from fibonacci.cached import fibonacci_cached, fibonacci_lru_cached
from fibonacci.dynamic import fibonacci_dynamic, better_fibonacci_dynamic
from typing import Callable
from conftest import time_tracker

# from my_decorator import my_parametrized


@pytest.mark.parametrize(
    "fib_func",
    [
        fibonacci_naive,
        fibonacci_cached,
        fibonacci_lru_cached,
        fibonacci_dynamic,
        better_fibonacci_dynamic,
    ],
)
@pytest.mark.parametrize("n,expected", [(0, 0), (1, 1), (2, 1), (20, 6765)])
# @my_parametrized(identifiers="n,expected", values=[(0, 0), (1, 1), (2, 1), (20, 6765)])
def test_fibonacci(
    time_tracker, fib_func: Callable[[int], int], n: int, expected: int
) -> None:
    res = fib_func(n)
    assert res == expected
