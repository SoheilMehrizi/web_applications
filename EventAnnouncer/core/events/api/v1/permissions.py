
"""
    Implemented Custom Permission classes.
    who and how can access the objects .
"""
from rest_framework import permissions

class IsOwnerOrReadOnly():
    """
    The User can only get the objects if he/she is not owner 
    otherwise he/she will be allowed to do all CRUD .
    """
    def IsOwnerOrReadOnly(self, request, view, obj):
        # Read Method is allowed for every requests,
        # So we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Instance must have an attribute named 'owner'
        # theres just person allowed to CUD the object who created it .
        return False
    