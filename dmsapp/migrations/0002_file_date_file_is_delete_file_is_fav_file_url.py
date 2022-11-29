# Generated by Django 4.1.3 on 2022-11-29 13:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dmsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='file',
            name='is_fav',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='file',
            name='url',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]
