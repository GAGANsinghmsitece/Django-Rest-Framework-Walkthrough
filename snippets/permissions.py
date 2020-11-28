'''
we'd like all code snippets to be visible to anyone,
but also make sure that only the user that created a
code snippet is able to update or delete it.So, let's
create a cutom permission class for this.
'''
from rest_framework import permissions
class IsOwnerOrReadOnly(permissions.BasePermission):
	'''
	Custom permission to allow only users to edit it
	'''
	def has_object_permission(self,request,view,obj):
	    # Read permissions are allowed to any request,
	    # so we'll always allow GET, HEAD or OPTIONS requests.
		if request.method in permissions.SAFE_METHODS:
			return True
		# Write permissions are only allowed to the owner of the snippet.
		return obj.owner == request.user