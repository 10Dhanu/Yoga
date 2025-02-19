from django.shortcuts import render
from django.http import JsonResponse
from .models import YogaClass
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import json

# Home Page
def home(request):
    return render(request, 'app/index.html')

def hatha_yoga(request):
    return render(request, 'app/hatha_yoga.html')

def ashtanga_yoga(request):
    return render(request, 'app/ashtanga_yoga.html')

def face_yoga(request):
    return render(request, 'app/face_yoga.html')

def parent_child_yoga(request):
    return render(request, 'app/parent_child_yoga.html')

def meditation_detox(request):
    return render(request, 'app/meditation_detox.html')

# Courses Page
def base(request):
    classes = YogaClass.objects.all()
    return render(request, 'app/base.html', {'classes': classes})

# About Page
def about(request):
    return render(request, 'app/about.html')

# Contact Page
def contact(request):
    return render(request, 'app/contact.html')



