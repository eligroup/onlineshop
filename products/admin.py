from django.contrib import admin
from .models import Product,Comment
from jalali_date.admin import ModelAdminJalaliMixin


class CommentInline(admin.TabularInline):# admin.StackedInline : change the view of admin panel
    model = Comment
    fields = ['author','body','stars','active']
    extra = 1 # create an empty tab


@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display = ['title','price','image','active',]
    inlines = [
        CommentInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author','product','body','stars','active']
    actions = ['approve_comments']

    def approve_comments(self,request,queryset):
        queryset.update(active=True)

# Register your models here.
