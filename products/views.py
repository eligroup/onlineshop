from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.shortcuts import render,get_object_or_404
from .models import Product, Comment
from .forms import CommentForm
from cart.forms import AddProductToCart


class ProductListView(generic.ListView):
    # model = Product
    queryset = Product.objects.filter(active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'




#------------ first way : class base view -------------#


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs): # this method is for adding a context,line or... to model
        context = super().get_context_data(**kwargs) #default,context include all product information
        context['comment_form'] = CommentForm() # in addition to product information send form that its name is comment_form
        # context['add_to_cart_form'] = AddProductToCart() # as we used of our html for this form it is not necssary to send this form
        return context #now product information and form as a new context will be shown

# for showing all comment in the same template there are 2 ways : 1- make a  new template view and in form action in template
# we give a new address that in its view the form will be saved and add to database then redirect again to detail template
# 2- we should do some stuff that product detail view be able to receive post request.
# if we want to have 2 forms in a template we can define two view and then in action give an address and in url get address and in its
# view do sth


class CommentDetailView(SuccessMessageMixin,generic.CreateView):
    model = Comment
    form_class = CommentForm
    success_message = "comment was created successfully"

    def form_valid(self, form): # default, this method call super form_valid in createview means, "return super().valid_form(form)
        #but we want to say before saving sent information in form ,add user and product on it

        new_comment = form.save(commit=False) # make an object of form and save it but not save in database,
        new_comment.author = self.request.user # we give user to form info
        product_id = int(self.kwargs['product_id']) # by this code we get product_id from url and make it int.
        product= get_object_or_404(Product,id=product_id) # find a product that its id is equal to product_id
        new_comment.product= product # new_comment is an object of comment . we set it equal to found product
        # as we need to define a success url we can use "DEF GET_SUCCESS_URL(SELF)" or add "def get_absolute_url
        return super().form_valid(form)





#------------  second way : functional base view  --------------#

# def product_detail_view(request,pk):
#     product = get_object_or_404(Product,pk=pk)
#     template_name = 'products/product_detail.html'
#     comments = product.comments.filter(active=True)
#     new_comment = None
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.product = product
#             new_comment.author = request.user
#             new_comment.save()
#             comment_form = CommentForm()
#     else:
#         comment_form = CommentForm()
#
#     return render(request,template_name,{'product': product,
#                                          'new_comment': new_comment,
#                                          'comment_form': comment_form,
#                                          'comment': comments})
