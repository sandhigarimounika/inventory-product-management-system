from rest_framework.routers import DefaultRouter
from django.urls import path
from .models import *
from .api_views import *
from .views import *
router=DefaultRouter()
router.register('product',ProductViewSet)
urlpatterns=[
    path('',dashboard,name='dashboard'),
    path('products/',product_list,name='product-list'),
    path('product/<int:id>/',product_detail,name='product_detail'),
path('add/',ProductCreateView.as_view(),name='add-product'),
    path('edit/<int:pk>/',ProductUpdateView.as_view(),name='edit-product'),
    path('delete/<int:pk>/',ProductDeleteView.as_view(),name='delete-product'),

    path('api/products/',ProductListCreateAPIView.as_view()),
    path('api/products/<int:pk>/',ProductDetailAPIView.as_view()),
]
urlpatterns+=router.urls