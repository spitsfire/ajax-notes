from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from . models import Note
from django.core import serializers
import json

# Create your views here.
def index(request):
    return render(request,'notes/index.html')

def all_html(request):
    return render(request, 'notes/snippet.html', { "notes": Note.objects.all() })

def create(request):
    Note.objects.create(content=request.POST['content'])
    return render(request, 'notes/snippet.html',{ "notes": Note.objects.order_by("-id") })