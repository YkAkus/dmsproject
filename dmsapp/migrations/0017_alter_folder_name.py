# Generated by Django 4.1.3 on 2022-12-31 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmsapp', '0016_alter_file_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='name',
            field=models.CharField(default='New_Folder', max_length=50, unique=True),
        ),
    ]
