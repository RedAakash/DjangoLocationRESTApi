from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=20)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=20)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=30)
    state = models.ForeignKey(State, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class LocationData(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
