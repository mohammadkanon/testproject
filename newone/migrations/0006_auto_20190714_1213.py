# Generated by Django 2.2.3 on 2019-07-14 06:13

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('newone', '0005_auto_20190714_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonemodel',
            name='phone',
            field=phone_field.models.PhoneField(default=1, max_length=20, unique=True),
            preserve_default=False,
        ),
    ]