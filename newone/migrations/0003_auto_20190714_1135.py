# Generated by Django 2.2.3 on 2019-07-14 05:35

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('newone', '0002_auto_20190714_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
            ],
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
