from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)
    def comment_count(self): # for accessing the count of active comment in template
        return self.comments.filter(active=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])


class Comment(models.Model):
    PRODUCT_STARS = [('1','very bad'),
                     ('2', 'bad'),
                     ('3', 'normal'),
                     ('4', 'good'),
                     ('5', 'perfect'),
                     ]

    body = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE , related_name="comments")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE , related_name="comments")
    active = models.BooleanField(default=False)
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS)
    create_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('product_detail' , args=[self.product.id])
