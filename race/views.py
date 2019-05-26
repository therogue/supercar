# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

from random import randint

# Create your views here.
def index(request):
    drivers = Driver.objects.all()

    context = {
        'drivers' : drivers,
        'extra_message' : "this is rendered from a template!"
    }
    return render(request, 'race/index.html', context)

def driver_detail(request, driver_id):
    driver = Driver.objects.get(pk=driver_id) # primary key

    context = {
        'driver' : driver
    }

    return render(request, 'race/driver.html', context)

def start(request):
    race = Race()
    race.save()

    context = {}

    all_drivers = Driver.objects.all()
    max_speed = 0
    sitting_driver_id = randint(1, len(all_drivers))

    for driver in all_drivers:
        if driver.id == sitting_driver_id:
            context['sitting_driver'] = driver
        else:
            race.drivers.add(driver)
            if driver.car.speed > max_speed:
                race.winner = driver
                max_speed = driver.car.speed

    race.save()

    context['race'] = race
    context['race_drivers'] = race.drivers.all()

    return render(request, 'race/race.html', context)