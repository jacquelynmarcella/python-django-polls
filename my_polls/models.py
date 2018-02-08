from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_text = models.DateTimeField('date published')

	def __str__(self): #Changes what displays when we query so we dont get an object
		return self.question_text

	def was_published_recently(self):
		return self.pub_text >= timezone.now() - datetime.timedelta(days=1) #finds results published in last day



class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE) #Give it a model its a FK to (Question model)
	#Cascade does auto cleanup if someone deletes the question the choice refers to
	choice_text = models.CharField(max_length=100)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text


