from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from boards.models import Board

def home(request):
    return HttpResponse("Hello, this is our first Application!")
def newhome(request):
    return HttpResponse("And this is another page of ours: Happy NEW Rabbit Year!")

def emptypath(request):
    #return HttpResponse("This function handles EMPTY Path")
    return render(request, 'welcome.html')

def listboards(request):
    boards = Board.objects.all()
    boards_names = list()

    for board in boards:
        boards_names.append(board.name)

    #response_html = '<br>'.join(boards_names)

    #return HttpResponse(response_html)

    return render(request, 'listboards.html', {'boards': boards})
