from rest_framework import serializers
from snippets.models import Snippet
"""
API's in general accepts a request on a particular url called as "API endpoint".
Corresponding to request it received, it generate results/responses.API returns data in
a particular format for example, json/XML/HTML etc. Hence, we need to convert our database
instances into the suitable format or get object from request it received. That is where
Serializers come into picture.
Following example shows serializer for Snippet Model. We define the fields we want from models
The we override following methods:-
1)create():- This method is called when it received a request to create a object of type
             Snippet.We are creating object in database by overriding this method.
2)update():-This method is called when serializer received update request. The request also
            contains the instance which is to be updated. Hence we are updating instance and 
            saving the instance in database in this method.
Now go to modelserializer.py for reading more. 
"""
class SnippetSerializer(serializers.Serializer):
	id=serializers.IntegerField(read_only=True)
	title=serializers.CharField(required=False,allow_blank=True,max_length=100)
	code=serializers.CharField(style={'base_template':'textarea.html'})
	linenos=serializers.BooleanField(required=False)
	language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
	style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

	def create(self,validated_data):
		#It will return a new instance of object.Thus we are creating a new instance from Snippets Model
		return Snippet.objects.create(**validated_data)

	def update(self,instance,validated_data):
		instance.title=validated_data.get('title',instance.title)
		instance.code=validated_data.get('code',instance.code)
		instance.linenos = validated_data.get('linenos', instance.linenos)
		instance.language = validated_data.get('language', instance.language)
		instance.style = validated_data.get('style', instance.style)
		instance.save()
		return instance