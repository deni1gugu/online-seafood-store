from django.db import models

# Create your models here.

class Seafood(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey('SeafoodCategory', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    weight = models.FloatField(verbose_name='Вес')
    country = models.CharField(max_length=100, verbose_name='Страна происхождения', blank=True)
    processing_method = models.CharField(max_length=100, verbose_name='Способ обработки', blank=True)
    shelf_life = models.IntegerField(verbose_name='Срок годности')
    storage_conditions = models.CharField(max_length=255, verbose_name='Условия хранения')
    cooking_methods = models.CharField(max_length=255, verbose_name='Способы приготовления', blank=True)
    image = models.ImageField(upload_to='seafood_images', verbose_name='Изображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Морепродукт'
        verbose_name_plural = 'Морепродукты'
        
class SeafoodCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Родительская категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория морепродуктов'
        verbose_name_plural = 'Категории морепродуктов'