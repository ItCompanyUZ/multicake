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


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('number', 'status')


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('cake', 'date', 'number')



@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('image',)


@admin.register(models.Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('image',)

