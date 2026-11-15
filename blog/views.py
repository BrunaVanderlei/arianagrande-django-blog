from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


def home(request):
    return render(request, 'blog/index.html')


def about(request):
    return render(request, 'blog/about.html')


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'post_list': posts, 'object_list': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_create(request):
    if request.method == 'POST':
        post = Post.objects.create(
            title=request.POST.get('title'),
            content=request.POST.get('content'),
            image=request.POST.get('image', ''),
            color=request.POST.get('color') or '#ECDBE0',
        )
        return redirect('post_detail', pk=post.pk)
    return render(request, 'blog/post_form.html')


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.image = request.POST.get('image', '')
        post.color = request.POST.get('color') or '#ECDBE0'
        post.save()
        return redirect('post_detail', pk=post.pk)
    return render(request, 'blog/post_form.html', {'post': post})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})