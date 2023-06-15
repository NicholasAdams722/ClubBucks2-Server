"""View module for handling requests for item data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from clubbucksapi.models import Item


class ItemView(ViewSet):
    """Honey Rae API items view"""

    def list(self, request):
        """Handle GET requests to get all items

        Returns:
            Response -- JSON serialized list of items
        """

        items = Item.objects.all()
        serialized = itemSerializer(items, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single item

        Returns:
            Response -- JSON serialized item record
        """

        item = Item.objects.get(pk=pk)
        serialized = itemSerializer(item)
        return Response(serialized.data, status=status.HTTP_200_OK)


class itemSerializer(serializers.ModelSerializer):
    """JSON serializer for items"""
    class Meta:
        model = Item
        fields = ('id', 'name', 'item_type', 'description', 'price', 'image', 'quantity')