from rest_framework import serializers
from beacons.models import Location, Collection
from django.contrib.auth.models import User, Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('name', 'floor', 'type')

class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Collection
        fields = (
        'ObjectID', 'ObjectNumber', 'ImageFilename', 'ArtistName1', 'ArtistName2', 'ArtistName3', 'ArtistName4',
        'ArtistName5', 'ArtistName6', 'ArtistName7', 'TitleOfWork1', 'TitleOfWork2', 'TitleOfWork3', 'TitleOfWork4',
        'Date', 'DateSearchBegin', 'DateSearchEnd', 'Medium', 'Materials', 'Techniques', 'Support', 'Dimensions',
        'GalleryLocation', 'Geography', 'Latitude', 'Longitude', 'CreditLine', 'PMAURL')
