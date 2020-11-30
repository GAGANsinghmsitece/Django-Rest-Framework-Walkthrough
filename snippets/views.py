from snippets.models import Snippet
from snippets.serializers import SnippetSerializer,UserSerializer
from rest_framework import generics,permissions,renderers
from django.contrib.auth.models import User
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
"""
views are the points at which request is executed.Drf gives two decorators for function-based 
views which is @api_view and it accept a list of allowed calls at that endpoint, for ex:- GET, 
POST, DELETE, PUT. For class-based views, it provides APIView.
Since some operations like create,update,delete,list,detail are common for models. For such 
scnerios, DRF provides generics.
The code is pretty self-explanatory.
Let's take a look at how we declare URL's with such views, refer to urls.py.
DRF also provide viewsets. If you want to know about viewset refer to 'viewsets.py'.
"""

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