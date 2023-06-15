"""View module for handling requests for item_type data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from clubbucksapi.models import ItemType


class ItemTypeView(ViewSet):
    """Honey Rae API item_types view"""

    def list(self, request):
        """Handle GET requests to get all item_types

        Returns:
            Response -- JSON serialized list of item_types
        """

        item_types = ItemType.objects.all()
        serialized = item_typeSerializer(item_types, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single item_type

        Returns:
            Response -- JSON serialized item_type record
        """

        item_type = ItemType.objects.get(pk=pk)
        serialized = item_typeSerializer(item_type)
        return Response(serialized.data, status=status.HTTP_200_OK)


class item_typeSerializer(serializers.ModelSerializer):
    """JSON serializer for item_types"""
    class Meta:
        model = ItemType
        fields = ('id', 'item_type')