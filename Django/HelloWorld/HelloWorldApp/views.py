from django.shortcuts import render, render_to_response
from django.http import HttpResponse

# Create your views here.

def foo(request):
	return render_to_response("helloDJ/home.html",
                               {"Testing" : "My Name is Viren Parmar ",
                               "HelloHello" : "Hello Pythonnist for Django"})