from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """Test Api View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'uses HTTP methods as function(GET, POST, PUT, PATCH, DELETE)',
            'we are testing view here',
            'not other thing',
            'all of the text is for demo purpose'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a post request with name"""
        serializer = self.serializer_class(data=request.data)

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
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of an object"""
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        """Handle deletion of an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test view set"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return hello message with list"""

        a_viewset = [
            'uses HTTP methods as function(list, create, retrieve, update, partial_update)',
            'we are testing view here',
            'not other thing',
            'all of the text is for demo purpose'
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})
    
    def create(self, request):
        """Create hello message with name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'

            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object with primary key"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle update an object with primary key"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle partial update an object with primary key"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle delete an object with primary key"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profile"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)