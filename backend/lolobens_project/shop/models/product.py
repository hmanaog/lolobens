from django.db import models


class Product(models.Model):

    product = models.CharField(
        verbose_name='product name',
        max_length=100,
        blank=True,
        null=True,
    )

    price = models.IntegerField(
        verbose_name='price',
        blank=True,
        null=True,
    )

    stocks = models.IntegerField(
        verbose_name='quantity',
        blank=True,
        null=True,
    )

    image = models.ImageField(
        verbose_name='product image',
        blank=True,
        null=True
    )

    description = models.TextField(
        verbose_name='description',
        blank=True,
        null=True
    )

    date_added = models.DateTimeField(
        verbose_name='date added',
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.product}'
