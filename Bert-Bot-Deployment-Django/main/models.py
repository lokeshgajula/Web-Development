from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
	""" A Question is a particular instance of the bert qna """
	question = models.TextField(null=False)
	wiki_terms = models.CharField(max_length=200,null=False)
	wiki_text = models.TextField(null=False)
	answer = models.CharField(max_length=200)
	prediction_score = models.FloatField(default=0)
	owner=models.ForeignKey(User,on_delete=models.CASCADE)