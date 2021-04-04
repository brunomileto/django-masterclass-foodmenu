from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import MovieData
from django.core.paginator import Paginator

class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer
    
class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='action')
    serializer_class = MovieSerializer

class ComedyViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='comedy')
    serializer_class = MovieSerializer



def movie_list(request):
    movie_objects = MovieData.objects.all()

    # creating search/filter
    movie_search = request.GET.get('movie_name') # 'movie_name' name of the form
    if movie_search != '' and movie_search is not None:
        # this bellow, looks for the exact name
        # movie_objects = movie_objects.filter(name=movie_search)
        # name__icontais search for names that contains the filter
        movie_objects = movie_objects.filter(name__icontains=movie_search)


    # creating the pagination
    paginator = Paginator(movie_objects, 3)
    # get current page
    page = request.GET.get('page')
    # get items from particular page (It is going to fetch not all objects
    # but only the ones need to fill the current page)
    movie_objects = paginator.get_page(page)

    return render(request, 'movies/movie_list.html', {'movie_objects': movie_objects})











