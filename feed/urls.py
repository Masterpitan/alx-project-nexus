from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed_home, name='feed_home'),
    path('api/', views.api_page, name='api_page'),
]
