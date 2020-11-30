"""
If you want to view this project with class-based views and urlpatterns, Use
include('snippets.urls').
If you want to view this project with viewsets and urlpatterns, Use 
include('snippets.viewset_urls').
If you want to view this project with viewsets and Rest_Router, Use 
include('snippets.Rest_Router').
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('snippets.Rest_Router')),
]
