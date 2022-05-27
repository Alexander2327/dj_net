from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as f:
        data = csv.DictReader(f, delimiter=',')

        paginator = Paginator(list(data), 10)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        page_data = page.object_list
        context = {
            'bus_stations': page_data,
            'page': page,
        }
        return render(request, 'stations/index.html', context)
