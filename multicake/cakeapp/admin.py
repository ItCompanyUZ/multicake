from modeltranslation.admin import TranslationAdmin
from django.contrib import admin
from . import models


@admin.register(models.Cake)
class CakeAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'type')


@admin.register(models.CakeType)
class CakeTypeAdmin(TranslationAdmin):
    list_display = ('id', 'name',)


@admin.register(models.Filling)
class FillingAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'composition')


@admin.register(models.Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'image',)


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'status')


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'cake', 'date', 'number')



@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'image',)


@admin.register(models.Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('id', 'image',)

