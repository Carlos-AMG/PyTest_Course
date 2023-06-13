import json
import pytest
import unittest
from unittest import TestCase
from django.test import Client
from django.urls import reverse

@pytest.mark.django_db
class TestGetCompanies(TestCase):
    def test_zero_companies_should_return_empty_list(self)->None:
        client = Client()
        companies_url = reversed('companies-list')
        response = client.get(companies_url)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.content), [])

