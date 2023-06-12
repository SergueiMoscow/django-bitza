from django.urls import path, re_path

from rent import views

urlpatterns = [
    path('summary', views.summary, name='summary'),
    path('payments', views.payments, name='payments'),
    path('clients', views.clients, name='clients'),
    path('contracts', views.contracts, name='contracts'),
    re_path(r'contacts/list', views.query_contacts, name='query_contacts'),
]