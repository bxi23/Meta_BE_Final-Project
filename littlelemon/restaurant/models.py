from django.db import models

# can add validators to integer fields with [parameter -> validators=[MinValueValidtor(minval), MaxValueValidator(maxval)]]
# Create your models here.
class booking(models.Model):
    id = models.IntegerField(primary_key=True) #int(11)
    name = models.CharField(max_length=255) #varchar(255)
    no_of_guests = models.IntegerField() #int(6)
    booking = models.DateTimeField() #datetime

    def __str__(self):
        return str(self.id) + ": " + str(self.name)

class menu(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return str(self.id) + ": " + str(self.title)