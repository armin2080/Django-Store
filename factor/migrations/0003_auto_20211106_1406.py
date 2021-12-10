# Generated by Django 3.2.7 on 2021-11-06 14:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('factor', '0002_auto_20211106_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factors',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='factors',
            name='payment_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ پرداخت'),
        ),
    ]
