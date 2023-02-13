from encodings import search_function
from multiprocessing import context
from turtle import title
from unicodedata import category
from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from main.functions import paginate_instances


from posts.models import Posts, Category, Author


def index(request):
    posts = Posts.objects.filter(is_deleted=False,is_draft=False)

    categories = Category.objects.all()[:5]
    authors = Author.objects.all()

    q = request.GET.get('q')
    if q:
        posts = posts.filter(title__istartswith=q)

    search_authors = request.GET.getlist("author")
    print(search_authors)
    if search_authors:
        posts = posts.filter(author__in=search_authors)

    search_categories = request.GET.getlist("category")
    print(search_categories)
    if search_categories:
        posts = posts.filter(categories__in=search_categories).distinct()

    sort = request.GET.get("sort")
    if sort:
        if sort == "title-asc":
            posts = posts.order_by("title")
        elif sort == "title-desc":
            posts = posts.order_by("-title")
        elif sort == "date-asc":
            posts = posts.order_by("published_date")
        elif sort == "date-desc":
            posts = posts.order_by("-published_date")


    instances = paginate_instances(request, posts)

    context = {
        "title" : "Home Page",
        # "posts": instances,
        "instances": instances,
        "categories" : categories,
        "authors": authors,
    }
    return render(request, "web/index.html", context=context)


def post(request,id):
    instance = get_object_or_404(Posts.objects.filter(id=id))
    context = {
        "instance" :instance
    }
    return render(request, 'web/post.html', context=context)
