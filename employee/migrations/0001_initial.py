# Generated by Django 4.1.1 on 2023-02-23 17:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicleID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('vehicleYear', models.IntegerField()),
                ('vehicleMake', models.CharField(max_length=64)),
                ('vehicleModel', models.CharField(max_length=64)),
                ('vehicleImage', models.ImageField(upload_to='vehicles')),
                ('vehiclePrice', models.IntegerField()),
                ('vehicleIsRetired', models.BooleanField(default=False)),
            ],
        ),
    ]
