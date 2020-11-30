from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User
"""
In the previous example, we created a serializer for Snippet Model(refer to simpleserializer.py),
but it involves lot of redundant code which tells type of model fields to serializer, as well as
methods we override. DRF provides ModelSerializer.py for such scnerios.
You can refer to following examples of ModelSerializer.
Refer to serializers.py for more.
"""
class UserSerializer(serializers.ModelSerializer):
	# adding a field for snippets by the user
	snippets=serializers.PrimaryKeyRelatedField(many=True,queryset=Snippet.objects.all())
	class Meta:
		model=User
		fields=['id','username','snippets']

class SnippetSerializer(serializers.ModelSerializer):
	owner=serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model=Snippet
		fields=['id','title','code','linenos','language','style','owner']