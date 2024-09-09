from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

class ProductCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        verbose_name = 'Котегория товара'
        verbose_name_plural = 'Котегория товаров'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)

    price = models.PositiveIntegerField(verbose_name='цена без скидки', help_text=' сомах')
    sales_procent = models.PositiveSmallIntegerField(
        verbose_name='скидка в процентах',
        null=True,
        blank=True,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ],
    )

    description = models.TextField()
    preview_imag = models.ImageField()

    new_expiry_date = models.DateField()

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


    def __str__(self):
        return self.name


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='product_gallery/')

    class Meta:
        verbose_name = 'Галерея товара'
        verbose_name_plural = 'Галерея товаров'

class ProductRating(models.Model):
    pass
