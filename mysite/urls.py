from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("inventary.urls")),
    path("rating/", include("rating.urls")),
    path("admin/", admin.site.urls),
]

handler404 = 'inventary.views.custom_404'
