# Generated by Django 4.2.4 on 2023-09-02 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_ingredients_alter_product_instructions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='item', max_length=200, unique=True),
        ),
    ]
