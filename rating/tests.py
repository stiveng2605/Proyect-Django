from django.test import TestCase, Client
from django.urls import reverse
from .models import Rating
from .forms import RatingForm


# ==================== TESTS DE MODELOS ====================

class RatingModelTest(TestCase):
    """Tests básicos para el modelo Rating"""
    
    def test_rating_creation(self):
        """Test de creación de rating"""
        rating = Rating.objects.create(
            name="Producto Excelente",
            comment="Muy bueno",
            score=5
        )
        self.assertEqual(rating.name, "Producto Excelente")
        self.assertEqual(rating.score, 5)
    
    def test_rating_str(self):
        """Test del método __str__"""
        rating = Rating.objects.create(name="Test", score=4)
        self.assertEqual(str(rating), "Test")


# ==================== TESTS DE FORMULARIOS ====================

class RatingFormTest(TestCase):
    """Tests básicos para RatingForm"""
    
    def test_form_valid(self):
        """Test de formulario válido"""
        form_data = {
            'name': 'Rating Test',
            'comment': 'Comentario',
            'score': 5
        }
        form = RatingForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_form_invalid(self):
        """Test de formulario inválido (sin campos requeridos)"""
        form_data = {}
        form = RatingForm(data=form_data)
        self.assertFalse(form.is_valid())


# ==================== TESTS DE VISTAS ====================

class RatingViewsTest(TestCase):
    """Tests básicos para vistas"""
    
    def setUp(self):
        self.client = Client()
        Rating.objects.create(name="Rating 1", score=5)
    
    def test_rating_list_view(self):
        """Test de vista de lista"""
        response = self.client.get(reverse('rating_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Rating 1')
    
    def test_rating_create_view_get(self):
        """Test de vista de creación (GET)"""
        response = self.client.get(reverse('rating_create'))
        self.assertEqual(response.status_code, 200)
    
    def test_rating_create_view_post(self):
        """Test de creación de rating (POST)"""
        form_data = {
            'name': 'Nuevo Rating',
            'comment': 'Comentario',
            'score': 4
        }
        response = self.client.post(reverse('rating_create'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Rating.objects.filter(name='Nuevo Rating').exists())