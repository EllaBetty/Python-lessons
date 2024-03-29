from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from boards.models import Board, Topic, Post
from boards.forms import NewTopicForm ### this line must be added!

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

def new_topic(request, pk): ## this function must be updated...
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})
