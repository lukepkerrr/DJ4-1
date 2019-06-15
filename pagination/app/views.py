import csv

from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    num_of_page = request.GET.get('page')
    if num_of_page is None:
        num_of_page = 1
    else:
        num_of_page = int(num_of_page)

    final_file = []
    with open(settings.BUS_STATION_CSV, encoding='cp1251') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            final_file.append({
                        'Name': row['Name'],
                        'Street': row['Street'],
                        'District': row['District']
                    })

    paginator = Paginator(final_file, 10)
    prev_num = None
    next_num = None
    if paginator.page(num_of_page).has_previous():
        prev_num = 'bus_stations?page={}'.format(paginator.page(num_of_page).previous_page_number())
    if paginator.page(num_of_page).has_next():
        next_num = 'bus_stations?page={}'.format(paginator.page(num_of_page).next_page_number())
    return render_to_response('index.html', context={
        'bus_stations': paginator.page(num_of_page),
        'current_page': num_of_page,
        'prev_page_url': prev_num,
        'next_page_url': next_num,
    })

