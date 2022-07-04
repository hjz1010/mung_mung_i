#from django.shortcuts import render

import json

from django.http import JsonResponse
from django.views import View

from .models import Owner, Dog


# Create your views here.
class OwnersView(View):
    def post(self, request):
        data = json.loads(request.body)
        name1 = Owner.objects.create(
            name=data['name'],
            email=data['email'],
            age=data['age']
        )
        Dog.objects.create(
            name=data['dog_name'],
            age=data['dog_age'],
            owner=name1
        )
        return JsonResponse({'message': 'created'}, status=201)
