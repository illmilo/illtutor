from django.shortcuts import render

from .models import About

# Create your views here.
def home(request):
    about = About.objects.all()
    return render(request, 'home/home.html', {'about': about})
def tutors(request):
    return render(request, 'home/tutors.html')