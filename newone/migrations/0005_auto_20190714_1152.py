# Generated by Django 2.2.3 on 2019-07-14 05:52

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('newone', '0004_auto_20190714_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonemodel',
            name='phone',
            field=phone_field.models.PhoneField(max_length=31, null=True),
        ),
    ]