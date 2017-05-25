from django.shortcuts import render
from django.http import HttpResponse


import urllib.request

# Create your views here.

def index(request):
	return render(request, 'newsfeed/index.html', {})

def bbcnews(request):
	response = urllib.request.urlopen('http://feeds.bbci.co.uk/news/rss.xml')
	return HttpResponse(response, 'text/xml')

def cnn(request):
	response2 = urllib.request.urlopen('http://rss.cnn.com/rss/cnn_topstories.rss')
	return HttpResponse(response2, 'text/xml')


