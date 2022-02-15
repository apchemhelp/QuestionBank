from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Question, AnswerChoice
import random

# Create your views here.
def get_questions(request):
	results = []
	questions = Question.objects.all()

	for q in questions:
		results.append(q.get_json())

	results = random.sample(results, len(results))

	return JsonResponse(results, safe=False)

def add_question(request):
	if request.method == "POST":
		question = request.POST["question"]
		unit = request.POST["unit"]

		choice_a = request.POST["a"]
		choice_b = request.POST["b"]
		choice_c = request.POST["c"]
		choice_d = request.POST["d"]
		choice_e = request.POST["e"]

		correct = request.POST["correct"]
		print(correct)

		question = Question.objects.create(type="MCQ", question=question, unit=int(unit))

		if len(choice_a) != 0:
			a = AnswerChoice.objects.create(text=choice_a)
			question.choices.add(a)
			if correct == "A":
				question.correct = a
		if len(choice_b) != 0:
			b = AnswerChoice.objects.create(text=choice_b)
			question.choices.add(b)
			if correct == "B":
				question.correct = b
		if len(choice_c) != 0:
			c = AnswerChoice.objects.create(text=choice_c)
			question.choices.add(c)
			if correct == "C":
				question.correct = c
		if len(choice_d) != 0:
			d = AnswerChoice.objects.create(text=choice_d)
			question.choices.add(d)
			if correct == "D":
				question.correct = d
		if len(choice_e) != 0:
			e = AnswerChoice.objects.create(text=choice_e)
			question.choices.add(e)
			if correct == "E":
				question.correct = e
		question.save()
		
		return HttpResponse("success")

	else:
		return render(request, "questions/add.html")
