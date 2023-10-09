from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
import pytest


@pytest.mark.django_db
def test_authorization():
    client = APIClient()
    url = reverse('token_obtain_pair')
    User.objects.create_user(username='yura', password='1234')
    data = {'username': 'yura', 'password': '1234'}
    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert 'access' in response.data
    assert 'refresh' in response.data

    refresh_token = response.data.get('refresh')
    url = reverse('token_refresh')
    data = {'refresh': refresh_token}
    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert 'access' in response.data
