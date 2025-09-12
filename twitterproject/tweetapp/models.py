from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Tweet(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField(max_length=255,blank=True,null=True)
    photo=models.ImageField(upload_to='photos/',blank=True,null=True)
    created_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(auto_now=True)
    likes=models.ManyToManyField(User,related_name='tweet_likes',blank=True)

    def __str__(self):
        return f'{self.user.username}-{self.text[:25]}'
    

    @property
    def total_likes(self):
        return self.likes.count()
    

    
class comment(models.Model):
    tweet=models.ForeignKey(Tweet,on_delete=models.CASCADE,related_name='comment')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    tweet_comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} is commented on {self.tweet.id}"
    
    
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profile_pics/',default='profile_pics/default.jpeg')
    bio=models.CharField(max_length=300)
    location=models.CharField(max_length=100,blank=True,null=True)
    joined_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} profile"
    

    