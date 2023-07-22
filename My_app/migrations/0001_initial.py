# Generated by Django 4.1 on 2023-07-17 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PredResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wind_speed', models.DecimalField(decimal_places=5, max_digits=10)),
                ('wind_direction', models.DecimalField(decimal_places=5, max_digits=10)),
                ('atmospheric_temperature', models.DecimalField(decimal_places=5, max_digits=10)),
                ('atmospheric_pressure', models.DecimalField(decimal_places=5, max_digits=10)),
                ('rotor_diameter', models.DecimalField(decimal_places=5, max_digits=10)),
                ('prediction', models.FloatField()),
            ],
        ),
    ]