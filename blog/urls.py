from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.posts, name='posts'),
    path('freebies', views.freebies, name='freebies'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('shop', views.shop, name='shop'),
    path('privacy', views.privacy, name='privacy'),
    path('conditions', views.conditions, name='conditions'),
    path('posts/<slug:slug>', views.single_post),
    path('freebies/<slug:slug>', views.single_freebie),
]