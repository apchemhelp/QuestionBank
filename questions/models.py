from django.db import models
import random

# Create your models here.
class AnswerChoice(models.Model):
	id = models.AutoField(primary_key=True)
	text = models.TextField()

class Question(models.Model):
	id = models.AutoField(primary_key=True)
	type = models.CharField(max_length=10) # FRQ, MCQ
	question = models.TextField()
	unit = models.IntegerField()
	choices = models.ManyToManyField(AnswerChoice)
	correct = models.OneToOneField(AnswerChoice, on_delete=models.CASCADE, related_name="correct", null=True)

	def get_json(self):
		c = random.sample(list(self.choices.all()), len(self.choices.all()))

		LETTERS = ["A", "B", "C", "D", "E"]
		choices = {}

		print(c)
		for i in range(len(c)):
			choices[LETTERS[i]] = c[i].text
	
		return {
			"id": self.id,
			"question": self.question,
			"unit": self.unit,
			"choices": choices,
			"correct": self.correct.text
		}

class Asset(models.Model):
	id = models.AutoField(primary_key=True)
	url = models.URLField()
	questions = models.ManyToManyField(Question)

