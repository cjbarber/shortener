from django.http import HttpResponse
from django.shortcuts import render_to_response, render, redirect
from shortener.models import Url

def index(request):
  urls = Url.objects.all()
  return render(request, "index.html", {'urls': urls})

def add(request):
  if request.method == "POST" and len(request.POST['expanded']) > 0:
    new_url = Url()
    new_url.expanded = request.POST['expanded']
    new_url.shortened = request.POST['shortened']
    new_url.save()
  return redirect('/')

def expand(request, shortened_url):
  url = Url.objects.get(shortened=shortened_url)
  return redirect(url.expanded)

def remove(request, url_id):
  url = Url.objects.get(id=url_id)
  url.delete()
  return redirect('/')