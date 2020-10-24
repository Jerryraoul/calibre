from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homePage(request):
    return HttpResponse("Well done. Your deployment was an success.")
