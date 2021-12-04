from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import *
from django.shortcuts import get_object_or_404

menu = [
    {'title': "Добавить человека", 'url_name': 'add'},
        {'title': "Войти в админку", 'url_name': 'login'}
]


class HumanViews(APIView):

    def post(self, request):
        serializer = HumanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, id=None):
        item = Human.objects.get(id=id)
        serializer = HumanSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        item = get_object_or_404(Human, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})

    def get(self, request, id=None):
        if id:
            item = Human.objects.get(id=id)
            serializer = HumanSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Human.objects.all()
        serializer = HumanSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


def index(request):
    posts = Human.objects.all()
    cats = Category.objects.all()
    return render(request, 'people/index.html', {'posts': posts, 'cats': cats, 'menu': menu, 'cat_selected': 0,
                                                 })


def add(request):
    return HttpResponse('Добавить человека')


def login(request):
    return HttpResponse('Войти в админку')


def person(request, post_id):
    return HttpResponse(f"Отображение человека с id = {post_id}")


def show_cat(request, cat_id):
    posts = Human.objects.all()
    cats = Category.objects.all()
    return render(request, 'people/index.html', {'posts': posts, 'cats': cats, 'menu': menu, 'cat_selected': cat_id,
                                                 })


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')




