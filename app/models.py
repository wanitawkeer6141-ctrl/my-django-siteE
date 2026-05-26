from django.db import models

# Create your models here.
class HOTEL(models.Model):
    name = models.CharField(max_length=100)
    price=models.IntegerField()
    image = models.ImageField(upload_to='app/')
    link=models.URLField()

    def __str__(self):
        return self.name


class fam(models.Model):
    image = models.ImageField(upload_to='app/')
    def __str__(self):
        return self.image.name if self.image else "No Image"

    # def __str__(self):
    #     return self.image

class Booking(models.Model):
    name = models.CharField(max_length=100)
    rooms = models.IntegerField()
    guests = models.IntegerField()
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.rooms} rooms"
