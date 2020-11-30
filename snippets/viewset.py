from snippets.models import Snippet
from snippets.serializers import SnippetSerializer,UserSerializer
from rest_framework import generics,permissions,renderers,viewsets
from django.contrib.auth.models import User
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import api_view,action
from rest_framework.reverse import reverse
"""
ViewSet classes are almost the same thing as View classes, except that they provide operations
such as retrieve, or update, and not method handlers such as get or put.
Here, we are replacing UserList and UserDetail view by a single UserViewSet.Similarly, we're 
replacing SnippetList and SnippetDetail view by a single SnippetViewSet. To replace 
SnippetHighlight view we extend SnippetViewSet to include a 'highight' method using @action 
decorator.
Now there are two ways to link urls with viewsets.
1)Use django urlpatterns:- This method is recommended if you want to have custom url endpoint 
names.
2)Use DRF Router:- DRF provides a Router which can create url endpoint with viewsets with 
logical naming.
To view usage with django urlpatterns, refer to viewset_url.py
To view usage with DRF router, refer to Rest_Router.py
"""
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