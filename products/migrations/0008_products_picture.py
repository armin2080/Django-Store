# Generated by Django 3.2.7 on 2021-12-08 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_products_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='picture',
            field=models.ImageField(default='/defaults/products.jpg', upload_to='products/'),
        ),
    ]
