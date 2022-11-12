from django.contrib import admin
from django.urls import path

from django_json_logging import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("log/", views.log),
]
