from django.shortcuts import render
from .models import Project

# Create your views here.


def home(request):
    projects = list(Project.objects.all())
    return render(request, 'portfolio/home.html', {"projects": projects})
