from django.db import models


class Marka(models.Model):
    marka_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.marka_name


class CarModel(models.Model):
    model_name = models.CharField(max_length=100, unique=True)
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name


class Car(models.Model):
    car_name = models.CharField(max_length=100)
    car_marka = models.ForeignKey(Marka, on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    year = models.DateField()
    millage = models.PositiveIntegerField()
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    COLOR = (
        ("КРАСНЫЙ", "Красный"),
        ("СИНИЙ", "Синий"),
        ("ЖЕЛНЫЙ", "Желтый"),
        ("ЧЕРНЫЙ", "Черный"),
    )
    color = models.CharField(max_length=9,
                             choices=COLOR,
                             default="ЧЕРНЫЙ")
    volume = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    have = models.BooleanField(default=True)
    description = models.TextField()
    image = models.ImageField(upload_to='img/', blank=True, null=True)
    video = models.FileField(upload_to='img/', blank=True, null=True)

    def __str__(self):
        return self.car_name
