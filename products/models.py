from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Grouping(models.Model):
    group = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.group


class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='product_cover/')
    group = models.ManyToManyField(Grouping, related_name='order')

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])


class LikeManage(models.Model):
    product = models.ForeignKey(Product, related_name='like', on_delete=models.CASCADE, null=True)
    like = models.BooleanField(default=False)


class Comment(models.Model):
    STAR = [
        ('1', 'very bad'),
        ('2', 'bad'),
        ('3', 'normal'),
        ('4', 'good'),
        ('5', 'very good')
    ]

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    star = models.CharField(max_length=10, choices=STAR)

    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=False)


