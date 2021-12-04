from rest_framework import serializers
from .models import *
import datetime


class HumanSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=50)
    surname = serializers.CharField(max_length=50)
    patronymic = serializers.CharField(max_length=50, allow_null=True)
    date_of_birth = serializers.DateField()
    passport = serializers.CharField(max_length=20)
    address = serializers.CharField(max_length=150)
    email = serializers.CharField(max_length=150)
    mobile = serializers.CharField(max_length=150)
    second_mobile = serializers.CharField(max_length=150, allow_null=True)
    photo = serializers.ImageField(allow_null=True)
    isu_number = serializers.IntegerField()
    vk_username = serializers.CharField(max_length=150)
    login_name = serializers.CharField(max_length=50)
    passwd_name = serializers.CharField(max_length=50)
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Human
        fields = ('__all__')


"""""
class CategorySerializer(serializers.ModelSerializer):
    cat = serializers.CharField(max_length=50)
    seccat = serializers.CharField(max_length=50, allow_null=True)
    thirdcat = serializers.CharField(max_length=50, allow_null=True)
    fourcat = serializers.CharField(max_length=50, allow_null=True)

    class Meta:
        model = Category
        exclude = ('__all__')
"""

