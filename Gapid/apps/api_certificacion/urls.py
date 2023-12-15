"""
URL configuration for Gapid project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework import routers
from .api import Perido_CertificacionViewsets
from .views import Periodo
from django.urls import path, include

router = routers.DefaultRouter()
router.register('api/Per', Periodo, basename='Periodo')

urlpatterns = [
    path('', include(router.urls)),
      path('reservacion/', ReservacionCreate.as_view(http_method_names=['get']), name='reservacion-list')
]