import json
from typing import List
import pytest

# from unittest import TestCase
# from django.test import Client
from django.urls import reverse
from api.coronavstech.companies.models import Company


# @pytest.mark.django_db
# class BasicCompanyAPITestCase(TestCase):
#     def setUp(self) -> None:
#         self.client = Client()
#         self.companies_url = reverse("companies-list")

#     def tearDown(self) -> None:
#         pass


# class TestGetCompanies(BasicCompanyAPITestCase):
#     def test_zero_companies_should_return_empty_list(self) -> None:
#         response = self.client.get(self.companies_url)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(json.loads(response.content), [])

#     def test_one_company_exists_should_suceed(self) -> None:
#         test_company = Company.objects.create(name="Amazon")
#         response = self.client.get(self.companies_url)
#         response_content = json.loads(response.content)[0]
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response_content.get("name"), test_company.name)
#         self.assertEqual(response_content.get("status"), "Hiring")
#         self.assertEqual(response_content.get("application_link"), "")
#         self.assertEqual(response_content.get("notes"), "")
#         test_company.delete()


# class TestPostCompanies(BasicCompanyAPITestCase):
#     def test_create_company_without_arguments_should_fail(self) -> None:
#         response = self.client.post(path=self.companies_url)
#         self.assertEqual(response.status_code, 400)
#         self.assertEqual(
#             json.loads(response.content), {"name": ["This field is required."]}
#         )

#     def test_create_company_repeated_should_fail(self) -> None:
#         Company.objects.create(name="apple")
#         response = self.client.post(path=self.companies_url, data={"name": "apple"})
#         self.assertEqual(response.status_code, 400)
#         self.assertEqual(
#             json.loads(response.content),
#             {"name": ["company with this name already exists."]},
#         )

#     def test_create_company_with_only_name_all_fields_should_be_default(self) -> None:
#         response = self.client.post(
#             path=self.companies_url, data={"name": "test company name"}
#         )
#         response_content = json.loads(response.content)
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(response_content.get("name"), "test company name")
#         self.assertEqual(response_content.get("status"), "Hiring")
#         self.assertEqual(response_content.get("application_link"), "")
#         self.assertEqual(response_content.get("notes"), "")

#     def test_create_company_with_layoffs_status_should_succeed(self) -> None:
#         response = self.client.post(
#             path=self.companies_url,
#             data={"name": "test company name", "status": "Layoffs"},
#         )
#         response_content = json.loads(response.content)
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(response_content.get("status"), "Layoffs")

#     def test_create_company_with_wrong_status_should_fail(self) -> None:
#         response = self.client.post(
#             path=self.companies_url,
#             data={"name": "test company name", "status": "WrongStatus"},
#         )
#         self.assertIn("WrongStatus", str(response.content))
#         self.assertIn("is not a valid choice", str(response.content))

#     @pytest.mark.xfail
#     def test_should_be_ok_if_fails(self) -> None:
#         self.assertEqual(2, 4)

#     @pytest.mark.skip
#     def test_should_be_skipped(self) -> None:
#         self.assertEqual(2, 4)


# def raise_covid19_exception() -> None:
#     raise ValueError("CoronaVirus Exception")


# def test_raise_covid19_exception_should_pass() -> None:
#     with pytest.raises(ValueError) as e:
#         raise_covid19_exception()
#     assert "CoronaVirus Exception" == str(e.value)


# import logging

# logger = logging.getLogger("CORONA_LOGS")


# def function_that_logs_something() -> None:
#     try:
#         raise ValueError("CoronaVirus Exception")
#     except ValueError as e:
#         logger.warning(f"I am logging {str(e)}")


# def test_logged_waring_level(caplog) -> None:
#     function_that_logs_something()
#     assert "I am logging CoronaVirus Exception" in caplog.text


# def test_logged_info_level(caplog) -> None:
#     with caplog.at_level(logging.INFO):
#         logger.info("I am logging info level")
#     assert "I am logging info level" in caplog.text

companies_url = reverse("companies-list")
pytestmark = pytest.mark.django_db


# ------------- Test Get Companies ---------------
def test_zero_companies_should_return_empty_list(client) -> None:
    response = client.get(companies_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []


def test_one_company_exists_should_suceed(client, amazon) -> None:
    response = client.get(companies_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert response_content.get("name") == amazon.name
    assert response_content.get("status") == "Hiring"
    assert response_content.get("application_link") == ""
    assert response_content.get("notes") == ""


# ------------- Test Post Companies ---------------
@pytest.mark.django_db
def test_create_company_without_arguments_should_fail(client) -> None:
    response = client.post(path=companies_url)
    assert response.status_code == 400
    assert json.loads(response.content) == {"name": ["This field is required."]}


def test_create_company_repeated_should_fail(client) -> None:
    Company.objects.create(name="apple")
    response = client.post(path=companies_url, data={"name": "apple"})
    assert response.status_code == 400
    assert json.loads(response.content) == {
        "name": ["company with this name already exists."]
    }


def test_create_company_with_only_name_all_fields_should_be_default(client) -> None:
    response = client.post(path=companies_url, data={"name": "test company name"})
    response_content = json.loads(response.content)
    assert response.status_code == 201
    assert response_content.get("name") == "test company name"
    assert response_content.get("status") == "Hiring"
    assert response_content.get("application_link") == ""
    assert response_content.get("notes") == ""


def test_create_company_with_layoffs_status_should_succeed(client) -> None:
    response = client.post(
        path=companies_url,
        data={"name": "test company name", "status": "Layoffs"},
    )
    response_content = json.loads(response.content)
    assert response.status_code == 201
    assert response_content.get("status") == "Layoffs"


def test_create_company_with_wrong_status_should_fail(client) -> None:
    response = client.post(
        path=companies_url,
        data={"name": "test company name", "status": "WrongStatus"},
    )
    assert "WrongStatus" in str(response.content)
    assert "is not a valid choice" in str(response.content)


@pytest.mark.xfail
def test_should_be_ok_if_fails() -> None:
    assert 2 == 4


@pytest.mark.skip
def test_should_be_skipped() -> None:
    assert 2 == 4


def raise_covid19_exception() -> None:
    raise ValueError("CoronaVirus Exception")


def test_raise_covid19_exception_should_pass() -> None:
    with pytest.raises(ValueError) as e:
        raise_covid19_exception()
    assert "CoronaVirus Exception" == str(e.value)


import logging

logger = logging.getLogger("CORONA_LOGS")


def function_that_logs_something() -> None:
    try:
        raise ValueError("CoronaVirus Exception")
    except ValueError as e:
        logger.warning(f"I am logging {str(e)}")


def test_logged_waring_level(caplog) -> None:
    function_that_logs_something()
    assert "I am logging CoronaVirus Exception" in caplog.text


def test_logged_info_level(caplog) -> None:
    with caplog.at_level(logging.INFO):
        logger.info("I am logging info level")
    assert "I am logging info level" in caplog.text


def test_workflow_works() -> None:
    assert 1 == 1


# ------------- Learn about fixtures tests ---------------


@pytest.mark.parametrize(
    "companies",
    [["TikTok", "Twitch", "Test Company INC"], ["Facebook", "Instagram"]],
    ids=["3 T companies", "Zuckerberg's companies"],
    indirect=True,
)
def test_multiple_companies_exists_should_suceed(client, companies) -> None:
    company_names = set(map(lambda x: x.name, companies))
    response_companies = client.get(companies_url).json()
    assert len(company_names) == len(response_companies)
    response_companies_names = set(
        map(lambda company: company.get("name"), response_companies)
    )
    assert company_names == response_companies_names
