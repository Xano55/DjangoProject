"""
Zadanie zaliczeniowe z Django
Imię i nazwisko ucznia: Piotr Malinowski
Data wykonania zadania: 28.03.2024
Treść zadania: Baza danych z filmami
Opis funkcjonalności aplikacji: Wyszukiwanie filmów z bazy danych za pomocą API MovieDB
"""

from django.contrib import admin
from django.urls import path
from moviedb import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main)
]
