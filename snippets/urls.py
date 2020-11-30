from django.urls import path,incslude
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
"""
When working with generics, using URL's is identical to using class-based views in Django.
Authentication for using the API is provided out-of-box by DRF by including 
'rest_framework.urls'.
DRF also provide content conversion which means our API can return data in a format 
requested, whether it's json,HTML,XML.To do so, add format=None in views and use
format_suffix_patterns with urlpatterns.
Now refer to viewset.py to learn about viewsets.s
"""
urlpatterns = [
    path('snippets/', views.SnippetList.as_view(),name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(),name='snippet-detail'),
    path('snippets/<int:pk>/highlight/',views.SnippetHighlight.as_view(),name='snippet-highlight'),
    path('users/', views.UserList.as_view(),name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(),name='user-detail'),
    path('api-auth/',include('rest_framework.urls')),
    path('', views.api_root),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
]
urlpatterns=format_suffix_patterns(urlpatterns)