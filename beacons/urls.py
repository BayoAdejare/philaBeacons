from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'collection', views.CollectionViewset)

app_name = 'beacons'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/', router.urls, name='api'),
]
