from rest_framework.test import APIClient
from faker import Faker
from myAPI.models import Message
import sys
import os
import pytest
from faker.providers import internet

faker = Faker()
faker.add_provider(internet)

sys.path.append(os.path.dirname(__file__))

@pytest.fixture
def client():
    '''fixture creates a client'''
    client = APIClient()
    return client

@pytest.fixture
def set_up():
    '''fixture creates 5 fake messages'''
    for _ in range(5):
        Message.objects.create(title=faker.name(), content=faker.text())







