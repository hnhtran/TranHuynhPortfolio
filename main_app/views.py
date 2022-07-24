from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("Hello, friends. You are at the front of my door. Please knock.")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("This is the about page. I am a software engineer.")
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')