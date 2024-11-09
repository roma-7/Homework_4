# Generated by Django 5.1.3 on 2024-11-09 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='car_name_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='car_name_tr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='description_tr',
            field=models.TextField(null=True),
        ),
    ]
