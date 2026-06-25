
from django.shortcuts import render

from rest_framework import viewsets
from .serializer import ProductSerializer

# Create your views here.
from django.views.generic import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Product
def dashboard(request):
    total_products=Product.objects.count()
    return render(request,'dashboard.html',{'total_products':total_products})
def product_list(request):
    products=Product.objects.all()
    return render(request,'product_list.html',{'products':products})
def product_detail(request,id):
    product = Product.objects.get(id=id)
    return render(request,'product_detail.html',{'product':product})
class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'product_form.html'
    success_url = reverse_lazy('product-list')

class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'product_form.html'
    success_url = reverse_lazy('product-list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product-list')

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
