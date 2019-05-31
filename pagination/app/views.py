import csv

from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.conf import settings


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    num_of_page = request.GET.get('page')
    if num_of_page is None:
        num_of_page = 1
    else:
        num_of_page = int(num_of_page)

    if num_of_page == 1:
        prev_num = None
    else:
        prev_num = 'bus_stations?page={}'.format(num_of_page - 1)
    next_num = 'bus_stations?page={}'.format(num_of_page + 1)

    list_for_response = []
    with open(settings.BUS_STATION_CSV) as csvfile:
        amount_for_skip = num_of_page * 10
        counter_for_skip = 0
        counter_for_print = 0
        reader = csv.DictReader(csvfile)
        for row in reader:
            if amount_for_skip != counter_for_skip:
                counter_for_skip += 1
            elif amount_for_skip == counter_for_skip:
                if counter_for_print != 10:
                    counter_for_print += 1
                    list_for_response.append({
                        'Name': row['Name'],
                        'Street': row['Street'],
                        'District': row['District']
                    })

    return render_to_response('index.html', context={
        'bus_stations': list_for_response,
        'current_page': num_of_page,
        'prev_page_url': prev_num,
        'next_page_url': next_num,
    })

