# Generated by Django 4.1.1 on 2023-10-11 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0039_alter_product_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productimage',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
