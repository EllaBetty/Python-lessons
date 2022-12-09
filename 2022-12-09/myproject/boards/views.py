from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, this is our first Application!")
def newhome(request):
    return HttpResponse("And this is another page of ours")


