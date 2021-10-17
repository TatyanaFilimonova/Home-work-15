from django.urls import path

from . import views

urlpatterns = [
path('articles/<str:name>', views.ArticlesView.as_view()),
path('articles/<str:name>/lastupdate/<lastupdate>', views.ArticlesFreshView.as_view()),
path('articles', views.ArticlesViewFilter.as_view()),
path('sports', views.SportsView.as_view()),
#path('sport/<sport>/last-modified/<lastmodified>', views.get_fresh_sport_feed, name='get_fresh_sport_feed'),
]