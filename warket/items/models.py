from django.db import models
from django.core.validators import *

# Create your models here.
CURRENCY = [
        ('$', '$'),
        ('₽', '₽'),
        ('€', '€'),
    ]


class Products(models.Model):
    item = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(
        validators=[
            MinValueValidator(1, message='Some urgument'),
            MaxValueValidator(5, message='Too much'),
        ]
    )
    currency = models.CharField(choices=CURRENCY)
    image = models.ImageField(
        'Image',
        upload_to='warket',
        blank=True
    )

    def __str__(self):
        return f'{self.item} {self.price}'
