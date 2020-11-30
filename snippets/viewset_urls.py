from snippets.viewset import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path,include
"""
While using viewset, we will define individual view using viewset and which methods are allowed
with the view.
For example, in snippet_list, when we are doing a GET request, we will list the snippets and 
when we will be doing a POST request, we will create a new snippet.
After creating such declarations, we can simply bind them to urlpatterns with url endpoint of 
our choice.
If you want to know how to use DRF Router with viewsets, refer to Rest_Router.py
"""
snippet_list=SnippetViewSet.as_view({
	'get':'list',
	'post':'create'
})
snippet_detail=SnippetViewSet.as_view({
	'get':'retrieve',
	'put':'update',
	'patch':'partial_update',
	'delete':'destroy',
})
snippet_highlight = SnippetViewSet.as_view({
	'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
	'get': 'list'
})
user_detail = UserViewSet.as_view({
	'get': 'retrieve'
})
urlpatterns = format_suffix_patterns([
	path('', api_root),
	path('snippets/', snippet_list, name='snippet-list'),
	path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
	path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
	path('users/', user_list, name='user-list'),
	path('users/<int:pk>/', user_detail, name='user-detail')
])