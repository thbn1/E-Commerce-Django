# Generated by Django 4.1.1 on 2023-10-11 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0037_alter_product_productcards'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productcards',
            field=models.JSONField(),
        ),
    ]