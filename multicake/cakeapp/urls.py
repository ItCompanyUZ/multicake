from django.urls import path
from .views import MainView, ProductListView, DeliveryView, load_more, ProductDetailView, FillingView,\
    PortfolioView, CantactView, ProductFilterView

app_name = 'cakeapp'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('fillings/', FillingView.as_view(), name='fillings'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('product_filter/', ProductFilterView.as_view(), name='product_filter'),
    path('cantact/', CantactView.as_view(), name='cantact'),
    path('product/<int:pk>', ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('delivery/', DeliveryView.as_view(), name='delivery'),
    path('load/', load_more, name='load')

]