# Generated by Django 3.2.5 on 2021-08-02 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0003_productcard'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pricetable',
            options={'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.AlterModelOptions(
            name='productcard',
            options={'verbose_name': 'Описание услуг', 'verbose_name_plural': 'Описание услуги'},
        ),
        migrations.AlterField(
            model_name='productcard',
            name='prdct_description',
            field=models.TextField(verbose_name='Описание услуги'),
        ),
        migrations.AlterField(
            model_name='productcard',
            name='prdct_img',
            field=models.ImageField(blank=True, upload_to='product', verbose_name='Изображение услуги'),
        ),
    ]