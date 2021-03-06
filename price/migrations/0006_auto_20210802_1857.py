# Generated by Django 3.2.5 on 2021-08-02 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0005_auto_20210802_1838'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productcard',
            old_name='description',
            new_name='prdct_description',
        ),
        migrations.RenameField(
            model_name='productcard',
            old_name='title',
            new_name='prdct_title',
        ),
        migrations.RemoveField(
            model_name='productcard',
            name='img',
        ),
        migrations.AddField(
            model_name='productcard',
            name='prdct_img',
            field=models.ImageField(blank=True, upload_to='product', verbose_name='Изображение услуги'),
        ),
    ]
