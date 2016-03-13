from django.conf.urls import *
from rest_framework import routers
from beacons import views

router = routers.DefaultRouter()
router.register(r'collection', views.CollectionViewset)

urlpatterns = patterns('',
                       url(r'^api/', include(router.urls)),
                       )