# Generated by Django 4.1.2 on 2023-03-17 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0006_alter_reservation_carid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='carId',
            field=models.UUIDField(),
        ),
    ]
