from django.urls import path
from app2.views import *
app_name='app2'


urlpatterns=[
    path('indexapp2/',indexapp2,name='indexapp2'),
]