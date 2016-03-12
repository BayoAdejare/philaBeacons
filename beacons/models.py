import json
from django.db import models
from datetime import datetime

class User(models.Model):
    name = models.TextField()
    dept = models.TextField()
    clean_count = models.IntegerField(default=0)
    dirty_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['dirty_count']

    def __str__(self):
        return '%s id:%s' % (self.name, self.id)


class Beacon(models.Model):
  def import_beacons(request):
    f = open('PMAPowerofArtHackathon-ibeacons.json', 'r')
    data = json.load(f)
    print(data)

    def import_location():
        f = open('PMAPowerofArtHackathon-locations.json', 'r')
        data = json.load(f)
        print(data)

    def import_collection():
        f = open('PMAPowerofArtHackathon-collectiondata.json', 'r')
        data = json.load(f)
        print(data)




        name = models.TextField()
    is_clean = models.BooleanField(default=True)
    beacon_id = models.TextField()

    def __str__(self):
        return '%s id:%s' % (self.name, self.beacon_id)

    def to_dict(self):
        self_dict = self.__dict__
        r = {k: self_dict[k] for k in self_dict if k[0] != '_'}
        return r