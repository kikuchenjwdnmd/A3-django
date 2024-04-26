from django.http import HttpResponse
from django.shortcuts import render

from app import models


def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    user = models.Users.objects.filter(email=email)
    if user.exists():
        user = user[0]
        if user.password == password:
            return HttpResponse('successful')
        else:
            return HttpResponse('wrong password')
    else:
        return HttpResponse('user does not exist')
# Create your views here.
