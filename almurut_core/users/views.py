from django.shortcuts import render
from django.views import View


class UserMakeRegistrationView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST

        password1 = data[]

