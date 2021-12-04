from django.db import models
from django.urls import reverse


class Human(models.Model):

    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество', blank=True, default='')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    passport = models.CharField(max_length=20, verbose_name='Паспорт')
    address = models.CharField(max_length=150, verbose_name='Адрес')
    email = models.CharField(max_length=150, verbose_name='Email')
    mobile = models.CharField(max_length=150, verbose_name='Номер телефона')
    second_mobile = models.CharField(max_length=150, verbose_name='Второй номер телефона', blank=True, default='')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, default='', verbose_name='Фото')
    isu_number = models.IntegerField(verbose_name='Номер ИСУ')
    vk_username = models.CharField(max_length=150, verbose_name='Vk')
    login_name = models.CharField(max_length=50, verbose_name='Логин в системе N')
    passwd_name = models.CharField(max_length=50, verbose_name='Пароль в системе N')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, related_name='Category')
    # указываем класс многие к одному
    seccat = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True,
                               related_name='SecondCategory')
    thirdcat = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='ThirdCategory')
    fourcat = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='FourthCategory')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})  # маршрутизатор


class Category(models.Model):     # многие к одному
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})
