# Generated by Django 4.1.3 on 2022-12-22 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmsapp', '0012_fileview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileview',
            name='opened_when',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]