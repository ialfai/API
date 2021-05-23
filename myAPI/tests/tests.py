from django.test import TestCase
import pytest
from myAPI.models import Message
from faker import Faker
from myAPI.tests.utilis import faker

# Create your tests here.

@pytest.mark.django_db
def test_add_massage(client, set_up):
    messages_count = Message.objects.count()
    new_message = {
        'title': "wiadomosc testowa",
        'content': "treść testowa"
    }
    response = client.post('/messages/', new_message, format='json')
    assert response.status_code == 201
    assert Message.objects.count() == messages_count + 1
    for key, value in new_message.items():
        assert key in response.data
        assert response.data[key] == value


@pytest.mark.django_db
def test_delete_message(client, set_up):
    messages_count = Message.objects.count()
    message1 = Message.objects.first()
    response = client.delete(f'/messages/{message1.id}', {}, format='json')
    assert response.status_code == 204
    message_ids = [i.id for i in Message.objects.all()]
    assert message1 not in message_ids
    assert Message.objects.count() == messages_count - 1


@pytest.mark.django_db
def test_edit_message(client, set_up):
    message1 = Message.objects.first()
    response = client.get(f'/messages/{message1.id}', {}, format='json')
    message_data = response.data
    message_data['title'] = 'completely new title - edited'
    response = client.patch(f"/messages/{message1.id}", message_data, format='json')
    assert response.status_code == 200
    message_object = Message.objects.get(id=message1.id)
    assert message_object.title == 'completely new title - edited'


@pytest.mark.django_db
def test_read_only_messages(client, set_up):
    response = client.get('/messages-view')
    assert response.status_code == 200








