import uuid

from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render

import A3Django.common
from app import models


def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    user = models.Users.objects.filter(email=email)
    if user.exists():
        user = user[0]
        if user.password == password:
            token = str(uuid.uuid4())

            login_user = {
                'email': user.email,
                'age': user.age,
                'id': user.id,
                'username': user.username,
            }

            result = {
                'token': token,
                'userInfo': login_user,
            }

            cache.set(token, login_user, 60 * 60)

            return A3Django.common.success_data(result, 'ok')
        else:
            return A3Django.common.fail('password error')
    else:
        return A3Django.common.fail('user does not exist')


def register(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    username = request.POST.get('username')
    age = request.POST.get('age')

    if email and password and username and age:
        user = models.Users.objects.filter(email=email)
        if user.exists():
            return A3Django.common.fail('user already exist')
        else:
            models.Users.objects.create(email=email, password=password, username=username, age=age)
            return A3Django.common.success()
    else:
        return A3Django.common.fail('email, password, age and username are required')


def get_flights_page(request):
    flights = models.Flights.objects.all()

    flights_list = list(flights.values())

    for index, flight in enumerate(flights_list):
        flights_list[index]['startTime'] = flight['startTime'].strftime('%d.%m.%Y %H:%M:%S')
        flights_list[index]['endTime'] = flight['endTime'].strftime('%d.%m.%Y %H:%M:%S')
        flights_list[index]['price'] = float(flight['price'])
        flights_list[index]['tax'] = float(flight['tax'])

    return A3Django.common.success_data(data=flights_list)
