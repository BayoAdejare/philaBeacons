from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'location', views.LocationViewSet)
router.register(r'collection', views.CollectionViewSet)

app_name = 'beacons'

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    url(r'^$', views.index, name='index'),
]
