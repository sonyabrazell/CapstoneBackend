# Generated by Django 3.2.8 on 2021-12-21 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_rename_nontradtracker_ogtracker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_cover',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
