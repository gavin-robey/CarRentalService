# Generated by Django 4.1.2 on 2023-02-20 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reservation',
        ),
    ]