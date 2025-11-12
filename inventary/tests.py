from django.test import TestCase, Client
from django.urls import reverse
from decimal import Decimal
from .models import Product, Category, Supplier
from .forms import ProductForm, CategoryForm, SupplierForm


# ==================== TESTS DE MODELOS ====================

class SupplierModelTest(TestCase):
    """Tests básicos para Supplier"""
    
    def test_supplier_creation(self):
        """Test de creación de proveedor"""
        supplier = Supplier.objects.create(
            name="Proveedor Test",
            contact_person="Juan Pérez",
            phone="123456789",
            email="juan@test.com"
        )
        self.assertEqual(supplier.name, "Proveedor Test")
    
    def test_supplier_str(self):
        """Test del método __str__"""
        supplier = Supplier.objects.create(
            name="Test",
            contact_person="Juan",
            phone="123",
            email="test@test.com"
        )
        self.assertEqual(str(supplier), "Test")


class CategoryModelTest(TestCase):
    """Tests básicos para Category"""
    
    def test_category_creation(self):
        """Test de creación de categoría"""
        category = Category.objects.create(
            name="Electrónica",
            description="Productos electrónicos"
        )
        self.assertEqual(category.name, "Electrónica")
    
    def test_category_str(self):
        """Test del método __str__"""
        category = Category.objects.create(name="Test")
        self.assertEqual(str(category), "Test")


class ProductModelTest(TestCase):
    """Tests básicos para Product"""
    
    def setUp(self):
        self.supplier = Supplier.objects.create(
            name="Proveedor",
            contact_person="Juan",
            phone="123",
            email="juan@test.com"
        )
        self.category = Category.objects.create(name="Electrónica")
    
    def test_product_creation(self):
        """Test de creación de producto"""
        product = Product.objects.create(
            name="Laptop",
            category=self.category,
            price=Decimal('999.99'),
            quantity=10,
            supplier=self.supplier
        )
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.price, Decimal('999.99'))
    
    def test_product_str(self):
        """Test del método __str__"""
        product = Product.objects.create(
            name="Mouse",
            category=self.category,
            price=Decimal('29.99'),
            quantity=5,
            supplier=self.supplier
        )
        self.assertEqual(str(product), "Mouse")


# ==================== TESTS DE FORMULARIOS ====================

class ProductFormTest(TestCase):
    """Tests básicos para ProductForm"""
    
    def setUp(self):
        self.supplier = Supplier.objects.create(
            name="Proveedor",
            contact_person="Juan",
            phone="123",
            email="juan@test.com"
        )
        self.category = Category.objects.create(name="Electrónica")
    
    def test_product_form_valid(self):
        """Test de formulario válido"""
        form_data = {
            'name': 'Laptop',
            'category': self.category.id,
            'price': '999.99',
            'quantity': 10,
            'supplier': self.supplier.id
        }
        form = ProductForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_product_form_invalid(self):
        """Test de formulario inválido"""
        form_data = {'name': 'Laptop'}
        form = ProductForm(data=form_data)
        self.assertFalse(form.is_valid())


class CategoryFormTest(TestCase):
    """Tests básicos para CategoryForm"""
    
    def test_category_form_valid(self):
        """Test de formulario válido"""
        form_data = {'name': 'Electrónica', 'description': 'Test'}
        form = CategoryForm(data=form_data)
        self.assertTrue(form.is_valid())


class SupplierFormTest(TestCase):
    """Tests básicos para SupplierForm"""
    
    def test_supplier_form_valid(self):
        """Test de formulario válido"""
        form_data = {
            'name': 'Proveedor',
            'contact_person': 'Juan',
            'phone': '123',
            'email': 'juan@test.com'
        }
        form = SupplierForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_supplier_form_invalid_email(self):
        """Test de email inválido"""
        form_data = {
            'name': 'Proveedor',
            'contact_person': 'Juan',
            'phone': '123',
            'email': 'invalid'
        }
        form = SupplierForm(data=form_data)
        self.assertFalse(form.is_valid())


# ==================== TESTS DE VISTAS ====================

class ProductViewsTest(TestCase):
    """Tests básicos para vistas de productos"""
    
    def setUp(self):
        self.client = Client()
        self.supplier = Supplier.objects.create(
            name="Proveedor",
            contact_person="Juan",
            phone="123",
            email="juan@test.com"
        )
        self.category = Category.objects.create(name="Electrónica")
        self.product = Product.objects.create(
            name="Laptop",
            category=self.category,
            price=Decimal('999.99'),
            quantity=10,
            supplier=self.supplier
        )
    
    def test_product_list_view(self):
        """Test de lista de productos"""
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Laptop')
    
    def test_product_detail_view(self):
        """Test de detalle de producto"""
        response = self.client.get(reverse('product_detail', args=[self.product.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Laptop')
    
    def test_product_create_view_post(self):
        """Test de creación de producto"""
        form_data = {
            'name': 'Mouse',
            'category': self.category.id,
            'price': '29.99',
            'quantity': 50,
            'supplier': self.supplier.id
        }
        response = self.client.post(reverse('product_create'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Product.objects.filter(name='Mouse').exists())


class CategoryViewsTest(TestCase):
    """Tests básicos para vistas de categorías"""
    
    def setUp(self):
        self.client = Client()
        Category.objects.create(name="Electrónica")
    
    def test_category_list_view(self):
        """Test de lista de categorías"""
        response = self.client.get(reverse('category_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Electrónica')


class SupplierViewsTest(TestCase):
    """Tests básicos para vistas de proveedores"""
    
    def setUp(self):
        self.client = Client()
        Supplier.objects.create(
            name="Proveedor Test",
            contact_person="Juan",
            phone="123",
            email="juan@test.com"
        )
    
    def test_supplier_list_view(self):
        """Test de lista de proveedores"""
        response = self.client.get(reverse('supplier_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Proveedor Test')
