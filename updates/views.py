from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def updates(request):
    return render(request, 'updates/updates.html')


def shoppinglist(request):
    return render(request, 'updates/shoppinglist.html')


def feedback(request):
    return render(request, 'updates/feedback.html')




