from django.contrib import admin

from .models import *


class HuAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'photo')
    list_display_links = ('name', 'surname', 'photo')
    search_fields = ('name', 'surname')


class CaAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(Human, HuAdmin)
admin.site.register(Category, CaAdmin)
