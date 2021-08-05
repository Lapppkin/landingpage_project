from django.db import models

# Create your models here.
class ProductCard(models.Model):
    prdct_img = models.ImageField(upload_to='product', blank=True, verbose_name='Изображение услуги')
    prdct_title = models.CharField(max_length=250, verbose_name='Заголовок услуги')
    prdct_description = models.TextField(verbose_name='Описание услуги')

    def __str__(self):
        return self.prdct_title

    class Meta:
        verbose_name = 'Описание услуг'
        verbose_name_plural = 'Описание услуги'


class PriceCard(models.Model):
    pc_title = models.CharField(max_length=200, verbose_name='Название пакета')
    pc_value = models.CharField(max_length=20, verbose_name='Цена')
    pc_description = models.CharField(max_length=250, verbose_name='Описание')

    def __str__(self):
        return self.pc_title

    class Meta:
        verbose_name = 'Цена пакета услуг'
        verbose_name_plural = 'Цены пакетов услуг'


class PriceTable(models.Model):
    pt_title = models.CharField(max_length=250, verbose_name='Услуга')
    pt_old_price = models.CharField(max_length=200, verbose_name='Старая цена')
    pt_new_price = models.CharField(max_length=200, verbose_name='Новая цена')

    def __str__(self):
        return self.pt_title

    class Meta:
        verbose_name = 'Услуга и их цена'
        verbose_name_plural = 'Услуги и их цены'
