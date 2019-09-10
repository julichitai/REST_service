from django.conf.urls import *
from django.urls import path
from . import views

urlpatterns = [
    # url('^$', views.ItemType_list),
    url('^(?P<pk>.+)/$', views.ItemType_detail)
]

