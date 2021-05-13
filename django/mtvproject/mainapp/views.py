from django.shortcuts import render
from .models import Team

# Create your views here.
def home(request) :
    team = Team.objects.all()
    return render(request, 'home.html', {'team' : team})
