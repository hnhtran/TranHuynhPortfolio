from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Feedback
from .forms import FeedbackForm

# Create your views here.
feedback_form = FeedbackForm()
def home(request):
    # return HttpResponse("Hello, friends. You are at the front of my door. Please knock.")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("This is the about page. I am a software engineer.")
    return render(request, 'about.html', {
        'feedback_form': feedback_form
    })

def projects(request):
    return render(request, 'projects.html')

def add_feedback(request):
    form = FeedbackForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('about')