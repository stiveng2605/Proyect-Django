from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('createProducts', views.ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product_update'),

    path('createCategory', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
    path('category', views.CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category_update'),

    path('createSupplier', views.SupplierCreateView.as_view(), name='supplier_create'),
    path('suppliers', views.SupplierListView.as_view(), name='supplier_list'),
    path('suppliers/<int:pk>/', views.SupplierDetailView.as_view(), name='supplier_detail'),
    path('supplier/<int:pk>/delete/', views.SupplierDeleteView.as_view(), name='supplier_delete'),
    path('supplier/<int:pk>/edit/', views.SupplierUpdateView.as_view(), name='supplier_update'),
]