from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse


class Create(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Create')


class Upload(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Upload')


class Login(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Login')


class Logout(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Logout')


