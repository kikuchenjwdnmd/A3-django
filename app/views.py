import uuid

from django.core.cache import cache
from django.db.models import Q
from django.forms import model_to_dict
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
    min_price = request.GET.get('minPrice')
    max_price = request.GET.get('maxPrice')

    filters = Q()
    if min_price:
        filters &= Q(price__gte=min_price)
    if max_price:
        filters &= Q(price__lte=max_price)

    flights = models.Flights.objects.filter(filters)

    flights_list = list(flights.values())

    for index, flight in enumerate(flights_list):
        flights_list[index]['startTime'] = flight['startTime'].strftime('%Y.%m.%d %H:%M:%S')
        flights_list[index]['endTime'] = flight['endTime'].strftime('%Y.%m.%d %H:%M:%S')
        flights_list[index]['price'] = float(flight['price'])
        flights_list[index]['tax'] = float(flight['tax'])

    return A3Django.common.success_data(data=flights_list)


def get_user_info(request):
    token = request.headers.get('Authorization')
    login_user = cache.get(token)
    if login_user:
        return A3Django.common.success_data(login_user)
    else:
        return A3Django.common.fail('invalid token')


def update_user_info(request):
    token = request.headers.get('Authorization')
    login_user = cache.get(token)

    if login_user:

        user = models.Users.objects.get(id=login_user['id'])

        if 'age' in request.GET:
            user.age = request.GET.get('age')

        if 'username' in request.GET:
            user.username = request.GET.get('username')
        user.save()

        user_dict = model_to_dict(user)

        return A3Django.common.success_data(user_dict)
    else:
        return A3Django.common.fail('invalid token')


def update_user_password(request):
    token = request.headers.get('Authorization')
    login_user = cache.get(token)

    if login_user:
        user = models.Users.objects.get(id=login_user['id'])
        if 'password' in request.POST:
            user.password = request.POST.get('password')
            user.save()
            return A3Django.common.success()
        else:
            return A3Django.common.fail('please enter your password')
    else:
        return A3Django.common.fail('invalid token')

