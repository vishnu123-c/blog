from django.urls import path
from .views import home_view,detail_view,post_view

urlpatterns = [
    path('',home_view,name="home"),
    path('posts/<str:slug>/',detail_view,name="details"),
    path('new',post_view,name="newpost")
]