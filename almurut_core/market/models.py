from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=250)



class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)

    price = models.PositiveIntegerField(verbose_name='цена без скидки', help_text=' сомах')\
    sales_procent = models.PositiveSmallIntegerField(
        verbose_name='скидка в процентах',
        null=True,
        blank=True
        validators=[MaxValueValdator(100)]
    )

    description = models.TextField()
    preview_imag =models.ImageField()

    new_expiry_date = models.DateField()

    class Meta:
        verbose_name_prual = 'Товары'
        verbose_name = 'Товар'

class ProductGallery(models.Model):
    product = models.ForeignKey()



class ProductRating(models.Model):

