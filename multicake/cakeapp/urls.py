from django.urls import path
from .views import MainView, ProductListView, DeliveryView, load_more

app_name = 'cakeapp'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('product/<int:pk>/', ProductListView.as_view(), name='product_list'),
    path('delivery/', DeliveryView.as_view(), name='delivery'),
    path('load/', load_more, name='load')
    # path('product/<int:pk>/', views.productcake, name='product_list'),
    # path('json-list/<int:num_fillings>', views.JsonListView.as_view(), name='json-list')
]