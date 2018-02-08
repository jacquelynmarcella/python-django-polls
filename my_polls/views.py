from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import F
from .models import Question, Choice

# Create your views here.
def index(request):
	# return HttpResponse("You are at the index page")
	latest_question_list = Question.objects.order_by('-pub_text')[:5] # -pub_date is desc, take the top 5
	return render(request, 'my_polls/index.html', {'latest_question_list': latest_question_list }) # Now we can access the questions we pulled in index.html

def vote(request, question_id):
	# return HttpResponse("You are at the vote page")
	question = get_object_or_404(Question, pk=question_id) #pk is primary key from param
	return render(request, 'my_polls/vote.html', {'question':question})

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	# return HttpResponse("You are at the result page")
	return render(request, 'my_polls/results.html', {'question': question})

def process_vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'my_polls/vote.html', {'question': question, 'error_message': 'You need to select a choice'})
	else:
		selected_choice.votes += F('votes') + 1
		selected_choice.save()
		return redirect('/polls/{0}/results/'.format(question_id))
		# return HttpResponse("You are at the process vote page")