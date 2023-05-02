import datetime
from django.shortcuts import render, redirect
from .models import Task, Reg
from .forms import TaskForm, RegForm
from datetime import datetime


# Create your views here.
# куда перейти в зависимости от урл адреса
# хтмл странички для пользователя
# шаблоны

def index(request):
    tasks = Task.objects.order_by('-id')  # [:3] #список эл-тов
    regs = Reg.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks, 'regs': regs})


def about(request):
    return render(request, 'main/about.html')


def new_task(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверная форма!'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/new_task.html', context)


def new_reg(request):
    error = ''
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверная форма!'

    form = RegForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/new_reg.html', context)


def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()

    return redirect('home')

def delete_reg(request, pk):
    reg = Reg.objects.get(pk=pk)
    reg.delete()

    return redirect('home')