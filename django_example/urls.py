"""django_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import *
from rest_framework import routers
from RestService import views

router = routers.DefaultRouter()
router.register(r'players', views.PlayerViewSet)
router.register(r'locations', views.LocationViewSet)
router.register(r'inventory', views.ItemTypeList)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory/', include('Inventory.urls')),
    url(r'^', include(router.urls)),
    url(r'^accounts/', include('django.contrib.auth.urls'))
    # url(r'^api-auth/', include('rest-framework.urls', namespace='rest-framework'))
]
