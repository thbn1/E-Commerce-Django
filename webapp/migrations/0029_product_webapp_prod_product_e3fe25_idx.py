# Generated by Django 4.1.1 on 2023-08-10 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0028_remove_product_webapp_prod_product_e3fe25_idx'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['productname'], name='webapp_prod_product_e3fe25_idx'),
        ),
    ]