# Generated by Django 4.0.4 on 2022-05-30 11:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('category', models.IntegerField()),
                ('author', models.IntegerField()),
                ('date_created', models.DateTimeField(default=datetime.datetime.utcnow)),
            ],
        ),
    ]
