# Generated by Django 2.2.3 on 2019-07-13 11:53

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190713_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='books/covers/', validators=[home.models.validate_image]),
        ),
    ]