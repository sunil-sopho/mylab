from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Question

def index(request):
    q_list = Question.objects.all();
    template = loader.get_template('Assn/index.html')
    context = {
        'q_list': q_list,
        }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    ques = Question.objects.get(id=question_id)
    template = loader.get_template('Assn/detail.html')
    return HttpResponse(template.render({'ques': ques}, request))
    
