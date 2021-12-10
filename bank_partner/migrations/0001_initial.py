# Generated by Django 3.2.7 on 2021-11-01 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankPartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, default='', max_length=25, null=True, verbose_name='نام کاربری')),
                ('password', models.CharField(blank=True, default='', max_length=25, null=True, verbose_name='رمز عبور')),
                ('merchant_code', models.CharField(max_length=60, verbose_name='کد مرچنت')),
                ('token', models.CharField(max_length=100, verbose_name='توکن')),
                ('bank_name', models.CharField(max_length=60, verbose_name='نام بانک')),
            ],
        ),
    ]