from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group
import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import Room
from account.models import UserAccount
from django.views.decorators.csrf import csrf_exempt
from account.forms import AddUserForm,EditUserForm
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
    if room.status == Room.WAITING:
        room.status= Room.ACTIVE
        room.agent = request.user
        room.save()
    return render(request,'room.html',{
        'room':room
    })


@login_required
def delete_room(request,uuid):
    if request.user.has_perm('room.delete_room'):
        room = Room.objects.get(uuid=uuid)
        room.delete()
        
        messages.success(request,'The room was deleted!')
        return redirect('/chat-admin/')
        
    else:
        messages.error(request,'You do not have access to delete room!')
        return redirect('/chat-admin/')
        

@login_required
def user_detail(request,uuid):
    user = UserAccount.objects.get(pk=uuid)
    rooms = user.rooms.all()
    return render(request,'user_detail.html',{
        'user':user,
        'rooms':rooms
    })
    
    
@login_required
def edit_user(request,uuid):
    if request.user.has_perm('user.edit_user'):
        user = UserAccount.objects.get(pk=uuid)
        
        if request.method =='POST':
            form =EditUserForm(request.POST,instance=user)
            if form.is_valid():
                form.save()
                messages.success(request,'The changes was saved!!')
                return redirect('/chat-admin/')
        else:
            form  = EditUserForm(instance=user)
        
        return render(request,'edit_user.html',{
            'user':user,
            'form':form
        })
        
    else:
        messages.error(request,'You do not have access to edit users!')
        return redirect('/chat-admin/')
        
    
    
   
    
    
@login_required
def add_user(request):
    if request.user.has_perm('user.add_user'):
        if request.method =='POST':
            form = AddUserForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_staff = True
                user.set_password(request.POST.get('password'))
                user.save()
                
                if user.role == UserAccount.MANAGER:
                    group = Group.objects.get(name='Managers')
                    group.user_set.add(user)
                    
                messages.success(request,'The users was added!')
                return redirect('/chat-admin/')
        else:
            form = AddUserForm()
    
        return render(request,'add_user.html',{
            'form':form
        })
    else:
        messages.error(request,'You do not have access to add users!')
        
        return redirect('/chat-admin/')