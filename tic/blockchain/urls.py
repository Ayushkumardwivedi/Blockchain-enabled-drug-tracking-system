# blockchain/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('send_transaction/', views.send_transaction, name='send_transaction'),
]