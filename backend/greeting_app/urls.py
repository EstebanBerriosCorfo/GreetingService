from django.urls import path
from . import views

urlpatterns = [
    path('greetings/', views.get_greetings, name='greeting-list'),  # Ruta para obtener todos los saludos
    path('greetings/create/', views.create_greeting, name='greeting-create'),  # Ruta para crear un saludo
    path('greetings/<int:pk>/', views.get_greeting, name='greeting-detail'),  # Ruta para obtener un saludo por ID
    path('greetings/<int:pk>/update/', views.update_greeting, name='greeting-update'),  # Ruta para actualizar un saludo
    path('greetings/<int:pk>/delete/', views.delete_greeting, name='greeting-delete'),  # Ruta para eliminar un saludo
]

