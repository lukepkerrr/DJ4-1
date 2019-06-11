import datetime as dt
import os

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseNotFound

def file_list(request, date=''):
    template_name = 'index.html'
    files = []
    for serv_file in os.listdir(settings.FILES_PATH):
        file_info = os.stat('{}\{}'.format(settings.FILES_PATH, serv_file))
        ctime = dt.datetime.fromtimestamp(file_info.st_ctime)
        mtime = dt.datetime.fromtimestamp(file_info.st_mtime)
        files.append({
            'name': serv_file,
            'ctime': ctime,
            'mtime': mtime
        })
    if date == '':
        context = {
            'files': files
        }
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    else:
        filter_date = dt.datetime.strptime(date, '%Y-%m-%d').date()
        for one_file in files:
            print(one_file['ctime'])
            print(filter_date)
            if one_file['ctime'] != filter_date:
                files.remove(one_file)
        context = {
            'files': files,
            'date': filter_date  # Этот параметр необязательный
        }
    return render(request, template_name, context)

def file_content(request, name):
    try:
        with open('{}\{}'.format(settings.FILES_PATH, name)) as opened_file:
        # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
            return render(
                request,
                'file_content.html',
                context={'file_name': name, 'file_content': opened_file.read()}
            )

    except FileNotFoundError:
        return HttpResponseNotFound("Файл не найден")