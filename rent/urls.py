from django.urls import path

from rent import views

urlpatterns = [
    path('summary', views.summary, name='summary'),
    path('payments', views.payments, name='payments'),
    path('clients', views.clients, name='clients'),
    path('contracts', views.contracts, name='contracts'),
]