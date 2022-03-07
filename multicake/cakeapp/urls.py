from django.urls import URLPattern, path
from . import views

app_name = 'cakeapp'

urlpatterns = [
    path('main', views.PublisherDetailView.as_view(), name='main'),
    # path('json-list/<int:num_fillings>', views.JsonListView.as_view(), name='json-list')
]