from django.shortcuts import render
from .models import LearningJourney, AboutMe
# Create your views here.
# View for home page
def index(request):
    journey = LearningJourney.objects.all()
    return render(request, 'index.html', {'journey': journey})

# View for about me page
def aboutMe(request):
    about = AboutMe.objects.first()
    return render(request, 'aboutMe.html', {'about': about})