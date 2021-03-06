from django.shortcuts import render
from django.http import HttpResponse , Http404 # http4040 is for raising exception
from .models import Question
# Create your views here.

def index(request):
	latest_question_list=Question.objects.order_by("-pub_date")[:5] # minus for reverse of oldest list to recent 
	# this dict is passed to html template
	context={
	'latest_question_list':latest_question_list,
	}
	return render(request,'polls/index.html',context)

def detail(request,question_id):
	# if question_id doesnot exist so it throw error
	try:
		question=Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request,'polls/detail.html',{'question':question})


def results(request,question_id):
	response="You are looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request,question_id):
	return HttpResponse("You are voting on question %s" % question_id)