from django.urls import path
from .views import MainView, ProductListView, DeliveryView, load_more, ProductDetailView, AddBookView

app_name = 'cakeapp'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('product/<int:pk>', ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('delivery/', DeliveryView.as_view(), name='delivery'),
    path('load/', load_more, name='load')

]