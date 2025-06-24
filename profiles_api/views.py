from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HellowApiView(APIView): # base on the APIView class
    """TEST API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None): # request is the pass-in to the function
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data) # data is passed in from the request

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'Method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'Method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'Method': 'DELETE'})
