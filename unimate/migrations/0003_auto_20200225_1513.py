# Generated by Django 2.2.4 on 2020-02-25 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unimate', '0002_roommate_unimate_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roommate',
            name='apartment_type',
            field=models.CharField(choices=[('hostel', 'hostel'), ('self contain', 'self contain'), ('single room self contain', 'single room self contain'), ('two rooms self contain', 'two rooms self contain'), ('one bedroom flat', 'one bedroom flat'), ('two bedroom flat', 'two bedroom flat'), ('three bedroom flat', 'three bedroom flat')], default='self contain', max_length=30),
        ),
    ]
