from django.urls import path
from . import views

urlpatterns = [
    path('heaters/', views.list_heaters),
    path('heaters/add/', views.add_heater),
    path('compute-loss/', views.compute_loss),
    path('simulate-hour/', views.simulate),
]
