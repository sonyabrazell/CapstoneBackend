# Generated by Django 3.2.8 on 2021-12-17 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20211217_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_cover',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
