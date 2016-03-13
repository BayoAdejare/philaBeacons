from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField()
    collection = models.TextField()
    like_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)

class Collection(models.Models):
    ObjectID = models.CharField(max_length=128, null=False, blank=True, unique=True)
    ObjectNumber = models.CharField(max_length=128, null=False, blank=True, unique=True)
    ImageFilename = models.CharField(max_length=128, null=False, blank=True, unique=True)
    ArtistName1 = models.CharField(max_length=128, null=False, blank=True, unique=True)
    ArtistName2 = models.CharField(max_length=128, null=False, blank=True, unique=True)
    ArtistName3 = models.CharField(max_length=128, null=False, blank=True, unique=True)
    ArtistName4 = models.CharField(max_length=128, null=False, blank=True, unique=True)
    ArtistName5 = models.CharField(max_length=128, null=False, blank=True, unique=True)
    ArtistName6 = models.CharField(max_length=128, null=False, blank=True, unique=True)
    ArtistName7 = models.CharField(max_length=128, null=False, blank=True, unique=True)
    TitleofWork1 = models.CharField(max_length=128, null=False, blank=True, unique=True)
    TitleofWork2 = models.CharField(max_length=128, null=False, blank=True, unique=True)
    TitleofWork3 = models.CharField(max_length=128, null=False, blank=True, unique=True)
    TitleofWork4 = models.CharField(max_length=128, null=False, blank=True, unique=True)
    Date = models.CharField(max_length=128, null=False, blank=True, unique=True)
    DateSearchBegin = models.CharField(max_length=128, null=False, blank=True, unique=True)
    DateSearchEnd = models.CharField(max_length=128, null=False, blank=True, unique=True)
    Medium = models.CharField(max_length=128, null=False, blank=True, unique=True)
    Materials = models.CharField(max_length=128, null=False, blank=True, unique=True)
    Techniques = models.CharField(max_length=128, null=False, blank=True, unique=True)
    Support = models.CharField(max_length=128, null=False, blank=True, unique=True)
    Dimensions = models.CharField(max_length=128, null=False, blank=True, unique=True)
    GalleryLocation = models.CharField(max_length=128, null=False, blank=True, unique=True)
    Geography = models.CharField(max_length=128, null=False, blank=True, unique=True)
    Latitude = models.CharField(max_length=128, null=False, blank=True, unique=True)
    Longitude = models.CharField(max_length=128, null=False, blank=True, unique=True)
    CreditLine = models.CharField(max_length=128, null=False, blank=True, unique=True)
    PMAURL = models.CharField(max_length=128, null=False, blank=True, unique=True)


