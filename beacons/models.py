from django.db import models

global alias
global major
global minor


# Create your models here.
class Location(models.Model):
    name = models.IntegerField(default=0)
    floor = models.TextField()
    type = models.TextField()


class Collection(models.Model):
    ObjectID = models.CharField(max_length=128, null=False, blank=True, unique=True)
    ObjectNumber = models.CharField(max_length=128, null=False, blank=True, unique=True)
    ImageFilename = models.ImageField(upload_to="%Y/%m/%d")
    ArtistName1 = models.CharField(max_length=128, null=False, blank=True, unique=True)
    ArtistName2 = models.CharField(max_length=128, null=False, blank=True, unique=True)
    ArtistName3 = models.CharField(max_length=128, null=False, blank=True, unique=True)
    ArtistName4 = models.CharField(max_length=128, null=False, blank=True, unique=True)
    ArtistName5 = models.CharField(max_length=128, null=False, blank=True, unique=True)
    ArtistName6 = models.CharField(max_length=128, null=False, blank=True, unique=True)
    ArtistName7 = models.CharField(max_length=128, null=False, blank=True, unique=True)
    TitleOfWork1 = models.CharField(max_length=128, null=False, blank=True, unique=True)
    TitleOfWork2 = models.CharField(max_length=128, null=False, blank=True, unique=True)
    TitleOfWork3 = models.CharField(max_length=128, null=False, blank=True, unique=True)
    TitleOfWork4 = models.CharField(max_length=128, null=False, blank=True, unique=True)
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
    PMAURL = models.URLField(max_length=128, null=False, blank=True, unique=True)
