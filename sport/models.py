from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to="profiles/")
    phone = models.CharField(max_length=20)
    
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"
    
    
    
class Teams(models.Model):
    team1 = models.CharField(max_length=220)
    team2 = models.CharField(max_length=220)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return f"{self.team1} - {self.team2} = {self.category}"
    
    
        
class Games(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    teams = models.ForeignKey(Teams, on_delete=models.CASCADE)
    date = models.DateTimeField()
    stadium = models.CharField(max_length=200)
    ticket_price = models.DecimalField(max_digits=8, decimal_places=2)
    tickets_count = models.PositiveIntegerField()
    team1_score = models.PositiveIntegerField(null=True, blank=True)
    team2_score = models.PositiveIntegerField(null=True, blank=True)
    video = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=20, default='upcoming')
    
    def __str__(self):
        return f"{self.teams} - {self.date}"
    
    
    
    


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return f"{self.user} - {self.game}"
    
    