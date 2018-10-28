# Generated by Django 2.1.2 on 2018-10-27 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='vehicle',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='core.Vehicle'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='info',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
    ]