# Generated by Django 3.1.14 on 2023-04-08 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Room', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cubic_metres_of_water', models.FloatField()),
                ('water_price', models.FloatField()),
                ('electrict_number', models.FloatField()),
                ('electricity_price', models.FloatField()),
                ('discount', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('pay_status', models.BooleanField(default=False)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Room.room')),
            ],
        ),
    ]
