from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Move(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, editable=False)
    status = models.BooleanField(default=False)
    desc = models.TextField(max_length=300)
    notes = models.TextField(max_length=300, blank=True)
    move_date = models.DateTimeField()

    def __str__(self):
        return f"{self.desc} by {self.owner}"


class Place(models.Model):
    move_id = models.ForeignKey(Move, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, blank=True)
    notes = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.name} {self.address}"


class Item(models.Model):
    move_id = models.ForeignKey(Move, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    brand = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=30)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    care = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.quantity}x {self.brand} {self.name}"
