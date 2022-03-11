from django.urls import URLPattern, path
from . import views
from .views import PublisherDetailView, ProductListView, InfoView

app_name = 'cakeapp'

urlpatterns = [
    path('', PublisherDetailView.as_view(), name='main'),
    path('product/<int:pk>/', ProductListView.as_view(), name='product_list'),
    path('infopay/', InfoView.as_view(), name='infopay'),
    # path('product/<int:pk>/', views.productcake, name='product_list'),
    # path('json-list/<int:num_fillings>', views.JsonListView.as_view(), name='json-list')
]