# Generated by Django 4.1.2 on 2023-02-20 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='pickUpAddress',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='userId',
            field=models.CharField(max_length=30),
        ),
    ]