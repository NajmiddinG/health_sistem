from django.db import models


class Clinic(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=300)
    tell = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Department(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=30)
    tell = models.IntegerField()

    def __str__(self):
        return self.first_name


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=30)
    tell = models.IntegerField()

    def __str__(self):
        return self.first_name


class Application(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    message = models.TextField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=1)
    status = models.BooleanField(default=False)
