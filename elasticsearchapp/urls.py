from . import views
from django.urls import path, include

urlpatterns = [
    path('search/', views.search_blog, name='search_author')
]
