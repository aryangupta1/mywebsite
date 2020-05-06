from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'base/home.html')
def facebook(request):
    return render(request, 'facebook.com')
def facebook(request):
    context = {'facebook': 'https://www.facebook.com'}
    return render(request, 'facebook', context)