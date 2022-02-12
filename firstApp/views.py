from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def display(request):
    return HttpResponse("<h1>My First Django App!</h1>")


def displayDateTime(request):
    current_datetime = datetime.datetime.now()
    current_datetime_str = "Current Date and Time is " + str(current_datetime)
    return HttpResponse(current_datetime_str)
