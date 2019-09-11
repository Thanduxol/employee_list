# Generated by Django 2.2.3 on 2019-08-13 08:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('job_title', models.CharField(max_length=50)),
                ('employment_date', models.DateField(default=datetime.date.today)),
                ('description', models.TextField()),
                ('photo', models.ImageField(blank=True, upload_to='')),
            ],
            options={
                'ordering': ['id', 'first_name'],
            },
        ),
    ]
