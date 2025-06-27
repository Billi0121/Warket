from django.db import models

# Create your models here.

class Products(models.Model):
    item = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    image = models.ImageField(
        'Image',
        upload_to='warket',
        blank=True
    )

    def __str__(self):
        return f'{self.item} {self.price}'
