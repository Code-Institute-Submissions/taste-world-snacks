# Generated by Django 3.1.2 on 2020-11-05 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ingredients',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]