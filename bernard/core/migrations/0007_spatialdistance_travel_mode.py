# Generated by Django 2.1.2 on 2018-12-11 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20181121_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='spatialdistance',
            name='travel_mode',
            field=models.IntegerField(choices=[(0, 'driving'), (1, 'bicycling')], default=0),
        ),
    ]
