from django.shortcuts import render
from django.shortcuts import render_to_response
from beacons.serializers import CollectionSerializer
from beacons.permissions import IsOwnerOrReadOnly
from django.http import HttpResponse
from beacons.models import User, Collection
from django.template.loader import get_template
from django.template import Context


# Create your views here.
class CollectionViewset(viewsets.ModelViewset):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user

def index(request):
    '''
     give overview of user's collection
    '''
    all_users = User.objects.all()
    t = get_template('beacons/index.html')
    html = t.render(Context({
        'users':all_users,
        'name_count': len(all_users),
        'half_count': len(all_users)/2 + 1
    }))
    return HttpResponse(html)


