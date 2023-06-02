from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def generic(request):
    return render(request,'generic.html')


def facebook(request):
    return HttpResponse('<h1><center>THIS IS FACEBOOK PAGE</center></h1>')



