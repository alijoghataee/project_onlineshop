from django.contrib import messages
from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from .models import Product, Comment, Grouping
from .forms import CommentForm


class ProductListView(generic.ListView):
    queryset = Product.objects.filter(status=True)
    paginate_by = 10
    template_name = 'product/list_view.html'
    context_object_name = 'product'


@login_required
def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comment = product.comments.filter(active=True)
    group = product.group.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.author = request.user
            new_comment.save()
            messages.success(request, 'your comment success send')
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    return render(request, 'product/detail_view.html', context={
        'product': product,
        'comment': comment,
        'comment_form': comment_form,
        'order': group
    })


class CategoriesListView(generic.ListView):
    model = Grouping
    template_name = 'product/categories_list_view.html'
    context_object_name = 'categories'


def list_product_by_category(request, pk):
    products = Product.objects.filter(group__in=[pk])

    return render(request, 'product/categories_product.html', context={'products': products, })

# class ProductDetailView(generic.DetailView):
#     model = Product
#     template_name = 'product/detail_view.html'
#     context_object_name = 'product'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['comment_form'] = CommentForm()
#         return context
#
#
# class CommentCreateView(generic.CreateView):
#     model = Comment
#     form_class = CommentForm
#
#     def form_valid(self, form):
#         obj = form.save(commit=False)
#         obj.author = self.request.user
#         product_id = int(self.kwargs['pk'])
#         product = get_object_or_404(Product, id=product_id)
#         obj.product = product
#         return super().form_valid(form)
