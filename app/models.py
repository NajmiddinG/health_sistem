from django.db.models import models

class Clinic(models.Model):
    pass

class Department(models.Model):
    clinic = models.Foreignkey(Clinic, on_delete=models.CASCADE)

class Doctor(models.Model):
    department = models.Foreignkey(Department, on_delete=models.CASCADE)

class Client(models.Model):
    pass

class Application(models.Model):
    client = models.Foreignkey(Client,  on_delete=models.CASCADE)
    doctor = models.Foreignkey(Doctor,  on_delete=models.CASCADE)
    # message = models.Charfield()

