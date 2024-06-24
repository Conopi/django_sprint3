from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category


def post_list(request):
    posts = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    ).order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'posts': posts})


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug, is_published=True)
    posts = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')
    return render(
        request,
        'blog/category.html',
        {'category': category, 'posts': posts}
    )


def post_detail(request, post_id):
    post = get_object_or_404(
        Post, pk=post_id, is_published=True, pub_date__lte=timezone.now(),
        category__is_published=True
    )
    return render(request, 'blog/detail.html', {'post': post})
