from django.db import models

# Create your models here.
# Model to store personal learning journey
class LearningJourney(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
# Model to store about me details
class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    skills = models.CharField(max_length=200)

    def __str__(self):
        return self.name