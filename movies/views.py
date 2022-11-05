from django.http import Http404
from django.shortcuts import render, redirect
from .models import Movies, Background
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required


# rkhyefzvqbcp

@login_required
def index(request):
    user = request.user
    is_adulte = user.groups.filter(name='adulte').exists()
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Movies.objects.filter(title__contains=query_name)
            return render(request, 'index.html', context={"movies": results, "user": user})
    if is_adulte:
        list_movies = Movies.objects.all()
    else:
        list_movies = Movies.objects.exclude(genre__contains="adulte")
    page = request.GET.get('page')
    paginator = Paginator(list_movies, 12)
    try:
        list_movies = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        list_movies = paginator.page(page)
    except EmptyPage:
        list_movies = paginator.page(page)
    return render(request, 'index.html',
                  context={"movies": list_movies, 'paginator': paginator, "user": user, "vip": is_adulte})


@login_required
def detail(request, movie_id):
    try:
        movie = Movies.objects.get(pk=movie_id)
    except Movies.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'detail.html', context={'movie': movie})


@login_required
def best_movie(request):
    top_movie = Movies.objects.filter(top_film=True)
    return render(request, 'best_movie.html', context={'top_movie': top_movie})


def home(request):
    img = Background.objects.values_list('background_img', flat=True).get(pk=1)
    count_movies = Movies.objects.count()
    count_movies_adult = Movies.objects.filter(genre__contains="adulte").count()
    context = {'img': img, 'count': count_movies, 'count_movies_adult': count_movies_adult}
    return render(request, 'home.html', context)


def test_htmx(request):
    data_movies = Movies.objects.all()
    query_name = request.GET.get('search', None)
    print(query_name)
    if query_name:
        query_result = Movies.objects.filter(title__icontains=query_name)
        return render(request, 'test_htmx.html', context={"movies": query_result})

    # context = {"movies": query_result}
    return render(request, 'test_htmx.html', context={"movies": data_movies})
