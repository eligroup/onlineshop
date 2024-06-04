from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext,gettext_lazy as _


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'))
    price = models.PositiveIntegerField(default=0,verbose_name=_('price'))
    image = models.ImageField(verbose_name=_("product image"),upload_to="product/product_cover", blank=True)
    active = models.BooleanField(default=True, verbose_name=_('available'))
    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name=_('created date'))
    modified_datetime = models.DateTimeField(auto_now=True , verbose_name=_('modified date'))
    class Meta:
        verbose_name = "product"
        verbose_name_plural = _('products')

    def comment_count(self): # for accessing the count of active comment in template
        return self.comments.filter(active=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])

class ActiveCommentManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentManager,self).get_queryset().filter(active=True) # up to querset() is objects after that is new manager


class Comment(models.Model):
    PRODUCT_STARS = [('1',_('very bad')),
                     ('2', _('bad')),
                     ('3', _('normal')),
                     ('4', _('good')),
                     ('5', _('perfect')),
                     ]

    body = models.TextField(verbose_name=_('text comment'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE , related_name="comments" , verbose_name=_('product title'))
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE , related_name="comments" , verbose_name=_('user'))
    active = models.BooleanField(default=False, verbose_name=_('publish status'))
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS , verbose_name=_('point'))
    create_datetime = models.DateTimeField(auto_now_add=True , verbose_name=_("created date"))
    modified_datetime = models.DateTimeField(auto_now=True , verbose_name=_("modified date"))
    # manager
    objects = models.Manager() # without new manager this line will be define automaticly by django but if we want to have new manager thiese two lines are necessary
    active_comment_manager = ActiveCommentManager()
    # objects.all()
    # active_comment_manager.all()

    # custom manager is a manager that give us our query
    class Meta:
        verbose_name = "comment"
        verbose_name_plural = _("comments")

    def get_absolute_url(self):
        return reverse('product_detail' , args=[self.product.id])


