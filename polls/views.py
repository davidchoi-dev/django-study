from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question

def index(req):
  latest_questions = Question.objects.order_by('-pub_date')[:5]

  context = {
    "latest_question_list": latest_questions
  }

  return render(req, 'polls/index.html', context)

def detail(req, question_id):
  return HttpResponse("You're looking at question %s."%(question_id))

def results(request, question_id):
  response = "You're looking at the results of question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)