from django.shortcuts import render
from django.shortcuts import render_to_response
from beacons.serializers import UserSerializer, GroupSerializer, LocationSerializer, CollectionSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from beacons.models import Location, Collection
from django.template.loader import get_template
from django.template import Context


# Create your views here.
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


def index(request):
    '''
     give overview of user's collection
    '''
    all_users = User.objects.all()
    t = get_template('beacons/index.html')
    html = t.render(Context({
        'users': all_users,
        'name_count': len(all_users),
        'half_count': len(all_users) / 2 + 1
    }))
    return HttpResponse(html)
