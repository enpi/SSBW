from models import Restaurante
from django.http.response import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from serializers import RestaurantSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

from django.http import HttpResponse

restaurantes = Restaurante.objects

def data_request(request):
    data = 'Hola'
    return JsonResponse(data, safe=False)


def index(request):
    context= {"mensaje": "restaurantes!", 'restaurantes': restaurantes[:3]}
    return render(request, 'base.html', context)

@login_required
def like_restaurant(request):
    id_res = None
    result = 0

    if request.method == 'GET':
        id_res = request.GET.get('likes','')
    if id_res:
        restaurant = Restaurante.objects.get(id=id_res)
    if restaurant:
        result = restaurant.likes + 1
        restaurant.likes =  result
        restaurant.save()

    return HttpResponse(result)


# http://stackoverflow.com/questions/17221598/getting-mongoengine-and-django-rest-framework-to-play-nice
# MongoEngine with Django REST Framework

class RestaurantViewSet(generics.ListCreateAPIView):
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        return Restaurante.objects



@csrf_exempt
@api_view(['GET', 'POST'])
def api_restaurantes (request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        serializer = RestaurantSerializer(restaurantes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def api_restaurantes_detail(request, pk):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        restaurant = Restaurante.objects.get(id=pk)
    except Restaurante.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RestaurantSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

