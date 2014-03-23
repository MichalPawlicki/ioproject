from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Hello!")


def index_with_number(request, number):
    return HttpResponse(str(number))