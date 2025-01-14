from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # ...existing code...
    points = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    badges = models.ManyToManyField('Badge', blank=True)
    
    def is_gamification_working(self):
        return self.points >= 0 and self.level >= 1 and self.badges.exists()
    
    def display_gamification_status(self):
        if self.is_gamification_working():
            return f"Points: {self.points}, Level: {self.level}, Badges: {self.badges.count()}"
        else:
            return "Gamification system is not working properly."
    # ...existing code...

class Badge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # ...existing code...
