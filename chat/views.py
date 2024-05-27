from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import Room
from account.models import UserAccount
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    context={
        'chat':'chat'
    }
    return render (request,'index.html',context)
@csrf_exempt
@require_POST
def create_room(request,uuid):
    name = request.POST.get('name','')
    url = request.POST.get('url','')

    Room.objects.create(uuid=uuid,client=name,url=url)

    return JsonResponse ({'message':'room created'})


@login_required
def admin(request):
    rooms = Room.objects.all()
    users = UserAccount.objects.filter(is_staff =True)
    
    return render(request,'admin.html',{
        'rooms':rooms,
        'users':users
    })
    
    
@login_required
def room(request,uuid):
    room = Room.objects.get(uuid=uuid)
    return render(request,'room.html',{
        'room':room
    })