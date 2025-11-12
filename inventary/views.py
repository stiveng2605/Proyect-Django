from django.shortcuts import render, redirect
from .models import Supplier, Category, Product
from .forms import ProductForm , CategoryForm, SupplierForm
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

class ProductListView(ListView):
    model = Product
    template_name = 'inventary/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'inventary/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventary/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'inventary/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventary/product_edit.html'
    success_url = reverse_lazy('product_list')

class CategoryListView(ListView):
    model = Category
    template_name = 'inventary/category_list.html'
    context_object_name = 'categories'

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'inventary/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'inventary/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'inventary/category_edit.html'
    success_url = reverse_lazy('category_list')

class SupplierListView(ListView):
    model = Supplier
    template_name = 'inventary/supplier_list.html'
    context_object_name = 'suppliers'

class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'inventary/supplier_detail.html'
    context_object_name = 'supplier'

class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = 'inventary/supplier_confirm_delete.html'
    success_url = reverse_lazy('supplier_list')

class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'inventary/supplier_form.html'
    success_url = reverse_lazy('supplier_list')

class SupplierUpdateView(UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'inventary/supplier_edit.html'
    success_url = reverse_lazy('supplier_list')

def custom_404(request, exception):
    return render(request, '404.html', status=404)

# Create your views here.
