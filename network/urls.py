from django.urls import path
from . import views

urlpatterns = [
    path('heaters/', views.list_headers),
    path('heaters/add/', views.add_heater),
    path('compute-loss/', views.compute_loss),
]