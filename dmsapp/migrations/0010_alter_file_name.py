# Generated by Django 4.1.3 on 2022-12-15 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmsapp', '0009_rename_title_file_name_alter_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
