# Generated by Django 4.0.4 on 2022-06-15 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20220615_0319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='uppdated',
            new_name='updated',
        ),
        migrations.AddField(
            model_name='article',
            name='published',
            field=models.DateField(blank=True, null=True),
        ),
    ]