from django.urls import path
from . import views

urlpatterns = [
    path('bikes/', views.get_data_bikes, name='bikes')
]
