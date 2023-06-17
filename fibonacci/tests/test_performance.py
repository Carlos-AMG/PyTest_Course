from fibonacci.dynamic import better_fibonacci_dynamic
from conftest import track_performance
import pytest


@pytest.mark.performance
@track_performance
def test_performance():
    better_fibonacci_dynamic(1000)
