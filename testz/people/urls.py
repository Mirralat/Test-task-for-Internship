from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='base'),
    path('login/', login, name='login'),
    path('add/', add, name='add'),
    path('post/<int:post_id>/', person, name='post'),
    path('category/<int:cat_id>/', show_cat, name='category'),
    path('human/', HumanViews.as_view())
]
