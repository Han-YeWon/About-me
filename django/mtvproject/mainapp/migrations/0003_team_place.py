# Generated by Django 3.2 on 2021-05-13 08:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20210513_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='place',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
