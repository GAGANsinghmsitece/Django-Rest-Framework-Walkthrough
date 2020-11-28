from snippets.models import Snippet
from snippets.serializers import SnippetSerializer,UserSerializer
from rest_framework import generics,permissions,renderers,viewsets
from django.contrib.auth.models import User
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import api_view,action
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request,format=None):
	return Response({
		'users':reverse('user-list',request=request,format=format),
		'snippets':reverse('snippet-list',request=request,format=format)
		})

class UserViewSet(viewsets.ReadOnlyModelViewSet):
	"""
    This viewset automatically provides `list` and `retrieve` actions.
    """
	queryset=User.objects.all()
	serializer_class=UserSerializer

"""
	This viewset list,create,update,retrieve and destroy actions.
	we will also create a highlight actions.
	Custom actions which use the @action decorator will respond to GET requests by default.
	We can use the methods argument if we wanted an action that responded to POST requests.
"""
class SnippetViewSet(viewsets.ModelViewSet):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
	@action(detail=True,renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)