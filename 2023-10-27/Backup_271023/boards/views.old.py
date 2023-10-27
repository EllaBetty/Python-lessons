from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse
from boards.models import Board

#def home(request):
#    return HttpResponse("Hello, this is our first Application!")
def newhome(request):
    return HttpResponse("And this is another page of ours: Happy NEW Rabbit Year!")

def emptypath(request):
    #return HttpResponse("This function handles EMPTY Path")
    return render(request, 'welcome.html')

def home(request):
    boards = Board.objects.all()
    boards_names = list()

    for board in boards:
        boards_names.append(board.name)

    #response_html = '<br>'.join(boards_names)

    #return HttpResponse(response_html)

    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'topics.html', {'board': board})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'new_topic.html', {'board': board})
