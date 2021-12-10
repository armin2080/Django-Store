from django.db import models

# Create your models here.


class categories(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=50, verbose_name="نام دسته بندی")
    picture = models.ImageField(upload_to='categories/',default = '/defaults/products.jpg')


class subcategories(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=50, verbose_name="نام دسته بندی")
    parent = models.ForeignKey(categories, verbose_name="دسته بندی", on_delete=models.CASCADE)


class products(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام محصول")
    category = models.ForeignKey(subcategories, verbose_name="دسته بندی", on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0, blank=True, verbose_name="تعداد محصول")
    price = models.PositiveIntegerField(verbose_name="قیمت محصول")
    deleted = models.BooleanField(verbose_name="محصول حذف شده", blank=True, default=False)
    picture = models.ImageField(upload_to ="products/",default = '/defaults/products.jpg')
    


