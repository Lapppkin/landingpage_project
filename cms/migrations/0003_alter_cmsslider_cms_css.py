# Generated by Django 3.2.5 on 2021-07-30 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_cmsslider_cms_css'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmsslider',
            name='cms_css',
            field=models.CharField(default='-', max_length=250, null=True, verbose_name='CSS класс'),
        ),
    ]