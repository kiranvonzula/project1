from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def hydjobsinfo(request):
	s='<h1>Hyderabad jobs information</h1>'
	return HttpResponse(s)
def chennaijobsinfo(request):
	t='<h1>Chennai jobs information</h1>'
	return HttpResponse(t)
def nellorejobsinfo(request):
	r='<h1>Nellore jobs information</h1>'
	return 	HttpResponse(r)
    