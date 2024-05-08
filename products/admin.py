from django.contrib import admin
from .models import Product,Comment

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','active']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author','product','body','stars','active']
    actions = ['approve_comments']

    def approve_comments(self,request,queryset):
        queryset.update(active=True)

# Register your models here.
