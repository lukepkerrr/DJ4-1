import datetime as dt
import os

from datetime import datetime
from django.conf import settings
from django.shortcuts import render

def file_list(request, year=0, month=0, day=0):
    template_name = 'index.html'
    files = []
    for file in os.listdir(settings.FILES_PATH):
        file_info = os.stat('{}\{}'.format(settings.FILES_PATH, file))
        ctime = datetime.fromtimestamp(file_info.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
        mtime = datetime.fromtimestamp(file_info.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
        files.append({
            'name': file,
            'ctime': ctime,
            'mtime': mtime
        })
    if year == 0:
        context = {
            'files': files
        }
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    else:
        context = {
            'files': files,
            'date': dt.date(year, month, day)  # Этот параметр необязательный
        }
    return render(request, template_name, context)

def file_content(request, name):
    with open('{}\{}'.format(settings.FILES_PATH, name)) as file:
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
        return render(
            request,
            'file_content.html',
            context={'file_name': name, 'file_content': file.read()}
        )

