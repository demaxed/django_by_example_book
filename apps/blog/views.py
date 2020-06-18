from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from apps.blog.models import Post


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


class PostDetail(DetailView):
        model = Post

        def get(self, request, *args, **kwargs):
            post = get_object_or_404(
                Post,
                slug=kwargs['post'],
                status='published',
                publish__year=kwargs['year'],
                publish__month=kwargs['month'],
                publish__day=kwargs['day'],
            )
            return render(request, 'blog/post/detail.html', {'post': post})

#
# def post_detail(request, year, month, day, post):
#     post = get_object_or_404(
#         Post,
#         slug=post,
#         status='published',
#         publish__year=year,
#         publish__month=month,
#         publish__day=day,
#     )
#     return render(request, 'blog/post/detail.html', {'post': post})
