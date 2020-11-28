from snippets.models import Snippet
from snippets.serializers import SnippetSerializer,UserSerializer
from rest_framework import generics,permissions,renderers
from django.contrib.auth.models import User
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request,format=None):
	return Response({
		'users':reverse('user-list',request=request,format=format),
		'snippets':reverse('snippet-list',request=request,format=format)
		})

class SnippetHighlight(generics.GenericAPIView):
	queryset = Snippet.objects.all()
	renderer_classes = [renderers.StaticHTMLRenderer]

	def get(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)

class UserList(generics.ListAPIView):
	queryset=User.objects.all()
	serializer_class=UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset=User.objects.all()
	serializer_class=UserSerializer

class SnippetList(generics.ListCreateAPIView):
	queryset=Snippet.objects.all()
	serializer_class=SnippetSerializer
	permission_classes=[permissions.IsAuthenticatedOrReadOnly]

	def perform_create(self,serializer):
		'''
		perform_create() allow us to change the manner in which a instance is saved 
		and also handled any information which is implicit in incoming request.
		'''
		serializer.save(owner=self.request.user)
		'''
		now a additional field name owner which will a instance of user model will be
		sent to serializer
		'''

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes=[permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]