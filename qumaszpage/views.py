from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Opinion
from .forms import PostForm, OpinionForm

# Create your views here.

from django.http import HttpResponse


def main(request):
    return render(request, 'main.html')

def uslugi(request):
    return render(request, 'uslugi.html')

def kontakt(request):
    return render(request, 'kontakt.html')

def cennik(request):
    return render(request, 'cennik.html')

def onas(request):
    return render(request, 'onas.html')


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'conowego/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'conowego/post_detail.html', {'post': post})

def error_404_view(request, exception):
    data = {"name": 'Qumasz'}
    return render(request, '404.html', data)

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('conowego/post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'conowego/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('conowego/post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'conowego/post_edit.html', {'form': form})

def opinion_list(request):
    opinions = Opinion.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'opinie/opinie.html', {'opinions': opinions})


def opinion_new(request):
    if request.method == "OPINION":
        form = OpinionForm(request.OPINION, request.FILES)
        if form.is_valid():
            opinion = form.save(commit=False)
            opinion.author = request.user
            opinion.published_date = timezone.now()
            opinion.save()
            return redirect('opinion_list')
    else:
        form = OpinionForm()
    return render(request, 'opinie/opinion_edit.html', {'form': form})

def opinion_edit(request, pk):
    opinion = get_object_or_404(Opinion,pk=pk)
    if request.method == "OPINION":
        form = OpinionForm(request.OPINION, request.FILES, instance=opinion)
        if form.is_valid():
            opinion = form.save(commit=False)
            opinion.author = request.user
            opinion.published_date = timezone.now()
            opinion.save()
            return redirect('opinion_list')
    else:
        form = OpinionForm(instance=opinion)
    return render(request, 'opinie/opinion_edit.html', {'form': form})




