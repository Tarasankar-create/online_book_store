# Generated by Django 5.1.4 on 2025-01-29 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_book',
            name='Review',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
