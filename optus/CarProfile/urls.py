from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addCar/', views.addCar, name='addCar'),
    path('delete/<int:carId>', views.delete, name='delete'),
    path('edit/<int:carId>', views.edit, name='edit'),
    path('document/', views.document, name='document'),

]
