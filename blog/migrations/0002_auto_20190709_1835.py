# Generated by Django 2.2.3 on 2019-07-09 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='created_by',
            new_name='author',
        ),
    ]
