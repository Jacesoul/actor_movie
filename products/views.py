from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.views import View
from products.models import *


class ProductsView(View):
    def get(self, request):
        actors = Actor.objects.all()
        results = []
        for actor in actors:
            results.append(
                {
                    "first_name": actor.first_name,
                    "last_name": actor.last_name,
                    "date_of_birth": actor.date_of_birth
                }
            )
        return JsonResponse({'results': results}, status=200)
