# Generated by Django 3.2.7 on 2021-12-08 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_products_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='picture',
            field=models.ImageField(default='/defaults/products.jpg', upload_to='products/'),
        ),
    ]
