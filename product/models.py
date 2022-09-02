from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    title = models.CharField(max_length=45)
    parent = TreeForeignKey('self', on_delete=models.CASCADE(), related_name='children')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField(null=True)
    price = models.PositiveBigIntegerField()
    stock = models.PositiveIntegerField()
    Amount_sold = models.PositiveIntegerField()

    seller = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
