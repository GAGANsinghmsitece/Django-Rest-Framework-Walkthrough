from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User
"""
Hyperlinking a API is an important feature which makes our API easily navigable.
For example, SnippetSerializer has a field called highlight which contains highlighted code 
snippet. We are making it navigable by binding it to 'snippet-highlight' view which is defined 
in urls.py.
Similarly in UserSerializer,we want all its related snippet objects to hyperlink it. Hence,
we create a field snippets which is hyperlinked to 'snippet-detail' view which is again defined
in urls.py.
For creating such serializer, we use 'HyperlinkedModelSerializer' instead of 'ModelSerializer'.
If you want to know more about serializer, offical docs are a sure thing to go through:-
https://www.django-rest-framework.org/api-guide/serializers/

Now we will look at how views created using Drf.
refer to views.py 
"""
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
	owner=serializers.ReadOnlyField(source='owner.username')
	highlight=serializers.HyperlinkedIdentityField(view_name='snippet-highlight',format='html')

	class Meta:
		model=Snippet
		fields=['url', 'id', 'highlight', 'owner','title', 'code', 'linenos', 'language', 'style']

class UserSerializer(serializers.HyperlinkedModelSerializer):
	snippets=serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

	class Meta:
		model = User
		fields = ['url', 'id', 'username', 'snippets']

