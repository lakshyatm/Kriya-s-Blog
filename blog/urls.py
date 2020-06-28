"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from blog import views

app_name = 'blog'

urlpatterns = [
    url(r'^(?P<id>\d+)/post_edit/$', views.post_edit, name="post_edit"),
    url(r'^(?P<id>\d+)/post_delete/$', views.post_delete, name="post_delete"),
    url(r'^(?P<id>\d+)/favourite_post/$', views.favourite_post, name="favourite_post"),
    url(r'^(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.post_detail, name="post_detail"),
    url(r'^create/$',views.post_create, name= "post_create"),
    url(r'(?P<id>\d+)/(?P<slug>[\w-]+)/$',views.post_detail, name="post_detail"),
    url(r'edit_profile/$',views.edit_profile,name="edit_profile"),
    url(r'favourite/$', views.post_favourite_list , name="post_favourite_list"),
]
