from rest_framework import serializers
from beacons.models import Collection
from django.contrib.auth.models import User

class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Collection
        fields = ('ObjectID','ObjectNumber','ImageFilename','ArtistName1','ArtistName2','ArtistNam3','ArtistName4','ArtistName5','ArtistName6','ArtistName7','TitleofWork1','TitleofWork2','TitleofWork3','TitleofWork4','Date','DateSearchBegin','DateSearchEnd','Medium','Materials','Techniques','Support','Dimensions','GalleryLocation','Geography','Latitude','Longitude','CreditLine','PMAURL')
