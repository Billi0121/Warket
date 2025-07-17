from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User

# Create your models here.
CURRENCY = [
        ('$', '$')
    ]

MODEL = [
    ('NEW', 'NEW'),
    ('SEC', 'SECONDHAND CAR'),
    ('FOR PARTS', 'FOR PARTS'),
]

class Products(models.Model):
    item = models.CharField(validators=[
        MinLengthValidator(10),
        MaxLengthValidator(60)
    ])
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    price = models.FloatField(
        validators=[
            MinValueValidator(1.00, message='Some urgument'),
            MaxValueValidator(100000.00, message='Too much'),
        ],
    )
    currency = models.CharField(choices=CURRENCY)
    model = models.CharField(choices=MODEL)
    image = models.ImageField(
        'Image',
        upload_to='warket',
        blank=True
    )

    def __str__(self):
        return f'{self.item} {self.price}'
