from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductListView.as_view(), name="product_list"),
    #path("<int:pk>/", views.product_detail_view, name="product_detail"),
    path("<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    #product_id is an enterance parameter for this url and access from product.id in template,
    path('comment/<int:product_id>',views.CommentDetailView.as_view(), name="comment_create"),

]
