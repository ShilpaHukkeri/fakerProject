# Generated by Django 3.1.4 on 2020-12-28 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('roll', models.IntegerField()),
                ('marks', models.FloatField()),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
