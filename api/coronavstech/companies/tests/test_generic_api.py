import requests
import json
import pytest

testing_env_companies_url = "http://127.0.0.1:8000/companies/"


@pytest.mark.skip_in_ci
def test_zero_companies_django_agnostic() -> None:
    response = requests.get(url=testing_env_companies_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []

@pytest.mark.skip_in_ci

def test_create_company_with_layoffs_django_agnostic() -> None:
    response = requests.post(
        url=testing_env_companies_url,
        json={"name": "test company name", "status": "Layoffs"},
    )
    response_content = json.loads(response.content)
    assert response.status_code == 201
    assert response_content.get("status") == "Layoffs"
    cleanup_company(company_id=response_content["id"])

def cleanup_company(company_id: str) -> None:
    response = requests.delete(url=f"{testing_env_companies_url + str(company_id)}")
    assert response.status_code == 204