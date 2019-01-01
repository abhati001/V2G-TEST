from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

def index(request):
    todo = Todo.objects.all()[:10]
    context = {
        'todo':todo
    }
    return render(request, 'index.html', context)

def details(request, id):
    tod = Todo.objects.get(id=id)
    context = {
        'tod':tod
    }
    return render(request, 'details.html', context)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']
        tod = Todo(title=title, text=text)
        tod.save()
        return redirect('/todo')
    else:
        return render(request, 'add.html')
