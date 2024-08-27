
from django.urls import path
from . import views  # Import your views here

urlpatterns = [
    path('', views.some_view, name='some_view_name'),  # Example URL pattern
]