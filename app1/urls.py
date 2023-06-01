from django.urls import path
from app1.views import *
app_name='app1'

urlpatterns=[
    path('indexapp1/',indexapp1,name='indexapp1'),
]