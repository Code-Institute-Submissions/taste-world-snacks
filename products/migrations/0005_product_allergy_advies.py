# Generated by Django 3.1.2 on 2020-11-05 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20201105_0441'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='allergy_advies',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
