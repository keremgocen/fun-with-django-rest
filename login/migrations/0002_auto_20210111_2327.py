# Generated by Django 3.0.8 on 2021-01-11 23:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='pin_code',
            field=models.CharField(default='00000', max_length=5, unique=True, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]
