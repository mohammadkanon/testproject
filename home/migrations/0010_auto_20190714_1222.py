# Generated by Django 2.2.3 on 2019-07-14 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20190713_2022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='cropping',
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='books/covers/'),
        ),
    ]
