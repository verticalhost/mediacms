from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # ...existing code...
    points = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    badges = models.ManyToManyField('Badge', blank=True)
    
    def is_gamification_working(self):
        return self.points >= 0 and self.level >= 1 and self.badges.exists()
    # ...existing code...

class Badge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # ...existing code...
