"""bitza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from bitza import views, settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    # Маршруты API
    path('api/', include('api.api_urls', namespace='api')),

    # Маршруты FrontEnd Django
    path('main/', views.main, name='main'),
    path('', views.main),
    path('rent/', include('rent.urls', namespace='rent')),
    path('work/', include('work.urls', namespace='work')),
    path('electricity/', include('electricity.urls', namespace='electricity')),

    path('api/electricity/', include('electricity.api.urls', namespace='electricity_api')),
    path(settings.DEPLOY_ENDPOINT, views.deploy, name='deploy'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
