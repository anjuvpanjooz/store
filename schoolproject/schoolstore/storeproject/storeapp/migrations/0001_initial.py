# Generated by Django 4.2.2 on 2023-09-19 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('desc', models.CharField(blank=True, max_length=250)),
                ('sub_course', models.CharField(max_length=250)),
                ('duration', models.IntegerField(blank=True)),
            ],
        ),
    ]
