from django.shortcuts import render
from django.http import Http404

from .models import Thread, Comment
from .forms import ThreadForm, CommentForm


def index(request):
    """
    The homepage of the app.

    GET: Return all threads and render them.
    POST: Create a new thread with the form data.
    """
    if request.method == 'POST':
        form = ThreadForm(request.POST, request.FILES)
        if form.is_valid():
            thread = Thread(**form.cleaned_data)
            thread.save()
    else:
        form = ThreadForm()

    threads = Thread.get_all()
    return render(request, 'home.html', {'form': form, 'threads': threads})


def thread(request, thread_id):
    """
    The thread details page.

    GET: Return a thread info and its comments and render them.
    POST: Create a new comment to a thread with the form data.
    """
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = Comment(**form.cleaned_data)
            comment.save(thread_id)
    else:
        form = CommentForm()

    thread = Thread.get_object(thread_id)
    if not thread:
        raise Http404
    comments = Comment.get_all(thread_id)

    return render(request, 'thread.html', {'form': form, 'thread': thread, 'comments': comments})
