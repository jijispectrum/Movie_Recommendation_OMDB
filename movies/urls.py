from django.urls import path
from . import views

urlpatterns = [
                         # Home Page → Movie Search
    path('recommend/', views.recommend_movies, name='recommend_movies'),  # Recommendations
]
