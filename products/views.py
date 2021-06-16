from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse
from django.views import View
from products.models import *


# class ProductsView(View):
#     def get(self, request):
#         actors = Actor.objects.all()
#         results = []
#         for actor in actors:
#             movie_list = [x.movie.title for x in actor.actormovie_set.all()]
#             results.append(
#                 {
#                     "first_name": actor.first_name,
#                     "last_name": actor.last_name,
#                     "date_of_birth": actor.date_of_birth,
#                     "movie_title": movie_list,
#                 }
#             )
#         return JsonResponse({'results': results}, status=200)


class ProductsView(View):
    def get(self, request):
        movies = Movie.objects.all()
        results = []
        for movie in movies:
            actor_firstname = [
                x.actor.first_name for x in movie.actormovie_set.all()]
            results.append(
                {
                    "title": movie.title,
                    "release_date": movie.release_date,
                    "running_time": movie.running_time,
                    "actor_firstName": actor_firstname,
                }
            )
        return JsonResponse({'results': results}, status=200)
