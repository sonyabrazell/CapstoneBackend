# Generated by Django 3.2.8 on 2021-12-17 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_cover',
        ),
        migrations.AlterField(
            model_name='book',
            name='book_isbn',
            field=models.CharField(max_length=50),
        ),
    ]
