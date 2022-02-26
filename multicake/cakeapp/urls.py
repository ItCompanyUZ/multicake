from django.urls import URLPattern, path
from . import views

app_name = 'cakeapp'

urlpatterns = [
    path('main', views.main, name='main')
]