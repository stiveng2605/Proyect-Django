from django.apps import AppConfig


class InventaryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventary'

class RatingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rating'
