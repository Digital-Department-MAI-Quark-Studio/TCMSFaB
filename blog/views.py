from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Article
from .forms import ArticleForm, CommentForm

def home(request):
    query = request.GET.get('q')
    articles = Article.objects.all()
    if query:
        articles = articles.filter(Q(title__icontains=query) | Q(content__icontains=query))
    return render(request, 'home.html', {'articles': articles})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog:home')
        else:
            return render(request, 'login.html', {'error': 'Неверные имя пользователя или пароль'})
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Имя пользователя уже занято'})
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('blog:home')
    return render(request, 'register.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('blog:login')

@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            form.save_m2m()
            return redirect('blog:home')
    else:
        form = ArticleForm()
    return render(request, 'article/create.html', {'form': form})

@login_required
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk, author=request.user)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('blog:home')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'article/edit.html', {'form': form, 'article': article})

@login_required
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk, author=request.user)
    if request.method == 'POST':
        article.delete()
        return redirect('blog:home')
    return render(request, 'article/edit.html', {'article': article})

def view_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.all()
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            return redirect('blog:view_article', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'article/view.html', {'article': article, 'comments': comments, 'form': form})

@login_required
def like_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.likes += 1
    article.save()
    return redirect('blog:view_article', pk=pk)