from django.urls import path
from Django_Project.Application import views

urlpatterns = [
    path('units/', views.unit_list),
    path('units/<int:pk>/', views.unit_detail),
]