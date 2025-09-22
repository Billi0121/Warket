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
    item = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    price = models.FloatField(
        validators=[
            MinValueValidator(1.00, message='Some urgument'),
            MaxValueValidator(100000.00, message='Too much'),
        ],
    )
    Category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    currency = models.CharField(choices=CURRENCY, max_length=20)
    model = models.CharField(choices=MODEL, max_length=10)
    image = models.ImageField(
        'Image',
        upload_to='warket',
        blank=True
    )

    def __str__(self):
        return f'{self.item} {self.price}'


class Category(models.Model):
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug

class Categorylist(models.Model):
    slug = models.SlugField(unique=True)
    category_slug = models.ForeignKey("Category",on_delete=models.CASCADE,blank=False, null=False, related_name="category_slug")

    def __str__(self):
        return f'{self.slug}'

class Cart(models.Model):
    item = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, null=True, related_name='items')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self): 
        return f'{self.item}'
    
RATE = [
    ('5', 5),
    ('4', 4),
    ('3', 3),
    ('2', 2),
    ('1', 1),
]

class ProductRate(models.Model):
    rate = models.CharField(choices=(RATE), max_length=20)
    description = models.TextField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} | {self.product} | Rating:{self.rate }'
    
