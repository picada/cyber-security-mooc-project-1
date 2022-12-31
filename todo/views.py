from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.utils import timezone

from .models import ToDo

@login_required
def add(request):
    if request.method == "POST":
        title = request.POST.get('title')

        ## FLAW 3
        query = "INSERT INTO todo_todo (user_id, done, title) VALUES ('%s', '%s', '%s');" % (request.user.id, False, title)

        cursor = connection.cursor()
        ## FLAW 3 Fix: use cursor.execute() instead of cursors.executescript()
        cursor.executescript(query)
        
        ## FLAW 3 Fix: Uncomment the code below
        '''todo = ToDo(
            user=request.user,
            title=request.POST.get("title"),
        )
        todo.save()'''
        cursor.close()
    return redirect("/")

@login_required
def delete(request, id):
    todo = ToDo.objects.get(pk=id)

    ## FLAW 1 Fix: Uncomment the code below
    '''if todo.user != request.user:
        return HttpResponseForbidden()'''

    todo.delete()
    return redirect("/")


@login_required
def mark_done(request, id):
    todo = ToDo.objects.get(pk=id)
    
    ## FLAW 1 Fix: Uncomment the code below
    '''if todo.user != request.user:
        return HttpResponseForbidden()'''

    todo.done = not todo.done
    todo.save()
    return redirect("/")

@login_required
def todos(request):
    todos = ToDo.objects.filter(
         user=request.user, 
    )

    return render(
        request,
        "todos.html",
        {"todos": todos}
    )
