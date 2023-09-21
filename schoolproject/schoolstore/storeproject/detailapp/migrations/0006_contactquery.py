# Generated by Django 4.2.2 on 2023-09-21 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detailapp', '0005_alter_course_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250, unique=True)),
                ('DOB', models.CharField(blank=True, max_length=250)),
                ('age', models.TextField(blank=True)),
                ('gender', models.TextField()),
                ('phone_no', models.TextField()),
                ('email_id', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('dep', models.CharField(choices=[('computer_science', 'COMPUTER_SCIENCE'), ('commerce', 'COMMERCE'), ('science', 'SCIENCE'), ('humanities', 'HUMANITIES'), ('arts', 'ARTS')], max_length=30)),
                ('courses', models.CharField(choices=[('bca', 'BCA'), ('bcom', 'BCOM'), ('bsc', 'BSC'), ('bba', 'BBA'), ('bfa', 'BFA')], max_length=25)),
                ('purpose', models.CharField(choices=[('enquiry', 'ENQUIRY'), ('commerce', 'PLACEORDER'), ('return', 'RETURN')], max_length=20)),
                ('materials_provide', models.BooleanField(default=True)),
            ],
        ),
    ]
