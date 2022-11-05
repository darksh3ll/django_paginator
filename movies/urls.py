from django.urls import path
# Create your views here.
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/movies', views.index, name='index'),
    path('/best-movie', views.best_movie, name='best-movie'),
    path('<int:movie_id>/', views.detail, name='detail'),
]
