from django.conf.urls import url
from my_polls import views

urlpatterns = [
	# Matches /polls
	# This is the home route of this controller for /polls
	url(r'^$', views.index, name='index'),
	# Matches /polls/5/vote
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
	#Matches polls/5/vote/process
	url(r'^(?P<question_id>[0-9]+)/vote/process/$', views.process_vote, name='process'),
	# Match polls/5/results
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results')
]