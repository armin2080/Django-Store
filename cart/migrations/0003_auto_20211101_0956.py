# Generated by Django 3.2.7 on 2021-11-01 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_auto_20211019_1410'),
        ('cart', '0002_alter_cart_id_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='count',
            field=models.PositiveIntegerField(default=1, verbose_name='تعداد'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='id_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products', verbose_name='نام محصول'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نام کاربری'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total_price',
            field=models.PositiveIntegerField(verbose_name='مبلغ نهایی'),
        ),
    ]
