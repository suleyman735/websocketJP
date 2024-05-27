from django.contrib import admin

# Register your models here.
from .models import Room, Message
from account.models import UserAccount


admin.site.register(Room)
admin.site.register(Message)
admin.site.register(UserAccount)