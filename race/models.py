# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    speed = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.make, self.model)

class Driver(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return '{} "{}" driving a {}'.format(self.name, self.nickname, str(self.car))

class Race(models.Model):
    race_date = models.DateTimeField('race date', default=timezone.now)
    drivers = models.ManyToManyField(Driver)
    winner = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='winner', null=True)

    def __str__(self):
        result = 'Race on {}, winner is {}'.format(str(self.race_date), str(self.winner))
        return result