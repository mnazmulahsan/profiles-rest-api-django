from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test Api View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'uses HTTP methods as function(GET, POST, PUT, PATCH, DELETE)',
            'we are testing view here',
            'not other thing',
            'all of the text is for demo purpose'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})