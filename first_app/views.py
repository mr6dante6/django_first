import os
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    msg = f'Текущие дата и время: {current_time}<br><a href="/">На главную страницу</a>'
    return HttpResponse(msg)


def workdir_view(request):
    files = os.listdir('.')
    file_list = '<br>'.join(files)
    return HttpResponse(f'Содержимое рабочей директории:<br>{file_list}<br><a href="/">На главную страницу</a>')
