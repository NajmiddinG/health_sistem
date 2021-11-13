from django.db import models

class Login(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    tell = models.IntegerField(max_length=20)


class Pation(models.Model):
    name = models.ForeignKey(Login, on_delete=models.CASCADE)
    type = models.CharField(max_length=200)
    message = models.TextField(max_length=1000)
    pation_date = models.DateTimeField(null=True, blank=True)
    doctor_date = models.DateTimeField(null=True, blank=True)
    acsepted = models.BooleanField(default=False)

class Doctor(models.Model):
    name = models.ForeignKey(Login, on_delete=models.CASCADE)
    pation = models.ForeignKey(Pation, on_delete=models.CASCADE)
    acsepted = models.BooleanField(default=False)
    message = models.TextField(max_length=1000)


