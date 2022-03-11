from django.urls import URLPattern, path
from . import views
from .views import PublisherDetailView

app_name = 'cakeapp'

urlpatterns = [
    path('main/', PublisherDetailView.as_view(), name='main'),
    path('product/<int:pk>/', views.ProductListView.as_view(), name='product_list'),
    # path('json-list/<int:num_fillings>', views.JsonListView.as_view(), name='json-list')
]