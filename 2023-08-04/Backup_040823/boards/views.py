from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from boards.models import Board, Topic, Post
from boards.forms import NewTopicForm ### this line must be added!
from django.contrib.auth.decorators import login_required # July 9th
from boards.forms import PostForm #July 14th
from django.db.models import Count ## Aug 4th


def newhome(request):
    return HttpResponse("And this is another page of ours: Happy NEW Rabbit Year!")

def emptypath(request):
    #return HttpResponse("This function handles EMPTY Path")
    return render(request, 'welcome.html')

@login_required # added on July 9th
def home(request):
    boards = Board.objects.all()
    boards_names = list()

    for board in boards:
        boards_names.append(board.name)

    #response_html = '<br>'.join(boards_names)

    #return HttpResponse(response_html)

    return render(request, 'home.html', {'boards': boards})

@login_required # added on July 9th
def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk) ## Aug 4th
    topics = board.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1) # Aug 4th
    return render(request, 'topics.html', {'board': board, 'topics': topics}) # Aug 4th

@login_required # added on July 9th
def new_topic(request, pk): ## this function must be updated...
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = request.user  #July 9th. The user who requested this page
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user #July 9th The user who requested thid page
            )
            #return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
            return redirect('topic_posts', pk=pk, topic_pk=topic.pk)  # <- here July 14th
            # after creating a new topic we can be taket to either the list of all topics or to this specific topic
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})

@login_required # added on July 9th
def topic_posts(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk) # Aug 4th
    topic.views += 1
    topic.save()
    return render(request, 'topic_posts.html', {'topic': topic})
@login_required # added on July 14th
def reply_topic(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topic_posts', pk=pk, topic_pk=topic_pk)
    else:
        form = PostForm()
    return render(request, 'reply_topic.html', {'topic': topic, 'form': form})
