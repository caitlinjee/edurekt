# Generated by Django 3.1 on 2020-11-07 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20200912_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='modules',
        ),
        migrations.DeleteModel(
            name='TakeModule',
        ),
    ]