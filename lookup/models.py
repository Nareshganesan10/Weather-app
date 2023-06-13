from django.db import models

class CityModel(models.Model):
    city_id = models.AutoField(primary_key=True, auto_created=True)
    city = models.CharField(max_length=50)
    country =  models.CharField(max_length=50)
    population = models.IntegerField()

    def __str__(self):
        return self.city