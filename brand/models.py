from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.ForeignKey(Brand, related_name='cars', on_delete=models.CASCADE)
    model = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.brand.name} {self.model}"
