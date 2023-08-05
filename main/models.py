from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=False, null=True)
    content = models.TextField(unique=True, blank=False, null=True)
    user = models.CharField(max_length=100, default='test')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    

class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    content = models.TextField(unique=True, blank=False, null=True)
    user = models.CharField(max_length=100, default='test')
    
    def __str__(self):
        return self.question.title + ' - ' + self.content[:15]


class LikeMap(models.Model):
    user = models.CharField(max_length=100)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)