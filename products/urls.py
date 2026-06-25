from django.urls import path
from .models import *
from .api_views import *
from .views import *

urlpatterns=[
    path('',dashboard,name='dashboard'),
    path('products/',product_list,name='product-list'),
    path('product/<int:id>/',product_detail,name='product_detail'),
path('add/',ProductCreateView.as_view(),name='add-product'),
    path('edit/<int:pk>/',ProductUpdateView.as_view(),name='edit-product'),
    path('delete/<int:pk>/',ProductDeleteView.as_view(),name='delete-product'),

    path('products/',ProductListCreateAPIView.as_view()),
    path('products/<int:pk>/',ProductDetailAPIView.as_view()),
]