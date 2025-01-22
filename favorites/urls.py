from django.urls import path
from .views import FavoriteList, FavoriteDetail

urlpatterns = [
    path('favorites/', FavoriteList.as_view()),
]
