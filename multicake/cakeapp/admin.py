from modeltranslation.admin import TranslationAdmin
from django.contrib import admin
from . import models


@admin.register(models.Cake)
class CakeAdmin(TranslationAdmin):
    list_display = ('name',)


@admin.register(models.CakeType)
class CakeTypeAdmin(TranslationAdmin):
    list_display = ('name',)


@admin.register(models.Filling)
class FillingAdmin(TranslationAdmin):
    list_display = ('name', 'composition')


@admin.register(models.Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('image',)
