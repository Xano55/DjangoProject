"""
Zadanie zaliczeniowe z Django
Imię i nazwisko ucznia: Piotr Malinowski
Data wykonania zadania: 28.03.2024
Treść zadania: Baza danych z filmami
Opis funkcjonalności aplikacji: Wyszukiwanie filmów z bazy danych za pomocą API MovieDB
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
]