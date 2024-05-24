from django.urls import path,include,re_path
from .views import index


urlpatterns = [
    path('',index, name='index')  
]