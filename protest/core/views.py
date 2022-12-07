from django.shortcuts import render
import string
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string


def create_user_random(count):
    try:
        for x in range(count):
            username = 'user_{}'.format(get_random_string(length=5))
            email = '{}@test.com'.format(username)
            password = get_random_string(length=50)
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
        return "Usuario creados con exito!!!!"

    except Exception as e:
        return "Exception in create_user_random: " + str(e)