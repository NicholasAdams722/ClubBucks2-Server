"""View module for handling requests for transaction_item data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from clubbucksapi.models import TransactionItem
from clubbucksapi.models import Item
from clubbucksapi.models import Transaction

#! This is the view for a bridge table
class TransactionItemView(ViewSet):
    """Honey Rae API transaction_items view"""

    def list(self, request):
        """Handle GET requests to get all transaction_items

        Returns:
            Response -- JSON serialized list of transaction_items
        """

        transaction_items = TransactionItem.objects.all()
        serialized = TransactionItemSerializer(transaction_items, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single transaction_item

        Returns:
            Response -- JSON serialized transaction_item record
        """

        transaction_item = TransactionItem.objects.get(pk=pk)
        serialized = TransactionItemSerializer(transaction_item)
        return Response(serialized.data, status=status.HTTP_200_OK)

class TicketEmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('id', 'created_on', 'completed_on', 'user', 'total_amount', 'item')

class TicketCustomerSerializer(serializers.ModelSerializer):

    class Meta: 
        model= Item
        fields = ('id', 'name', 'item_type', 'description', 'price', 'image', 'quantity')

class TransactionItemSerializer(serializers.ModelSerializer):
    """JSON serializer for transaction_items"""
    transaction = TicketEmployeeSerializer(many=False)
    item = TicketCustomerSerializer(many=False)
    class Meta:
        model = TransactionItem
        fields = ('id', 'transaction', 'item', 'quantity')
        depth = 1