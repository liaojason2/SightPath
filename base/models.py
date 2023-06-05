from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"

class Room(models.Model):
    # 刪除使用者時不刪除該房間, 將值設為 null
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # 刪除話題時不刪除該房間, 將值設為 null
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # participants = 
    
    def __str__(self):
        return f"{self.name}"

class Message(models.Model):
    # 當使用者被刪除後，刪除訊息
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 當討論室被刪除後，刪除訊息
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.body[0:20]}"
    

class Competition(models.Model):
    name = models.CharField(max_length=100)
    href = models.TextField()
    # competition_img = models.ImageField()
    
    def __str__(self):
        return f"{self.name}"
    