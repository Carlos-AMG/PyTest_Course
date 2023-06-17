from django.core import mail
from django.urls import reverse
import json
import pytest

fibonacci_url = reverse("fibonacci")


@pytest.mark.parametrize("n,expected", [(0, 0), (1, 1), (2, 1), (20, 6765)])
def test_fibonacci_valid_input(client, n, expected) -> None:
    response = client.get(f"{fibonacci_url}?n={n}")
    assert response.status_code == 200
    assert json.loads(response.content) == {"n": n, "fibonacci": expected}


@pytest.mark.xfail
def test_fibonacci_invalid_input(client):
    response = client.get(f"{fibonacci_url}?n={-2}")
    assert response.status_code == 500
