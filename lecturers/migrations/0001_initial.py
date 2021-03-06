# Generated by Django 3.1 on 2020-09-12 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('staff_id', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('department', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=256)),
                ('module', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lecturers', to='modules.module')),
            ],
        ),
    ]
