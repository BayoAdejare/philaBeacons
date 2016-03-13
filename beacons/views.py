from django.shortcuts import render
from beacons.serializers import UserSerializer, GroupSerializer, LocationSerializer, CollectionSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from beacons.models import Location, Collection


# Create your views here.
def index(request):
    """
     Give overview of user's collection.
    """
    all_users = User.objects.all()
    all_groups = Group.objects.all()
    all_locations = Location.objects.all()
    all_collections = Collection.objects.all()
    html = {
        'users': all_users,
        'groups': all_groups,
        'locations': all_locations,
        'collections': all_collections
    }
    return render(request, 'beacons/index.html', html)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def pre_save(self, obj):
        assert isinstance(self.request.user, object)
        obj.owner = self.request.user


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    def pre_save(self, obj):
        assert isinstance(self.request.user, object)
        obj.owner = self.request.user
