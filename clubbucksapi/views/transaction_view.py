"""View module for handling requests for transaction data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from clubbucksapi.models import Transaction
from datetime import datetime
from rest_framework.decorators import action


class TransactionView(ViewSet):
    """Club Bucks API transactions view"""

    def list(self, request):
        """Handle GET requests to get all transactions

        Returns:
            Response -- JSON serialized list of transactions
        """

        transactions = Transaction.objects.all()
        serialized = TransactionSerializer(transactions, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single transaction

        Returns:
            Response -- JSON serialized transaction record
        """

        transaction = Transaction.objects.get(pk=pk)
        serialized = TransactionSerializer(transaction)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    
    @action(methods=['put'], detail=True)
    def complete(self, request, pk):
        """Complete an order by adding a payment type and completed data
        """
        try:
            order = Transaction.objects.get(pk=pk, user=request.auth.user)
            order.completed_on = datetime.now()

            #Bug: order needs to be "saved" as a new order with a unique id
            order.save()
            return Response({'message': "Order Completed"})
        except (Transaction.DoesNotExist) as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    @action(methods=['get'], detail=False)
    def current(self, request):
        """Get the user's current order"""
        try:
            transaction = Transaction.objects.get(
                completed_on=None, user=request.auth.user)
            serializer = TransactionSerializer(transaction)
            return Response(serializer.data)
        except Transaction.DoesNotExist:
            return Response({
                'message': 'You do not have an open order. Add a product to the cart to get started'},
                status=status.HTTP_404_NOT_FOUND
            )  

class TransactionSerializer(serializers.ModelSerializer):
    """JSON serializer for transactions"""
    class Meta:
        model = Transaction
        fields = ('id', 'user', 'created_on', 'completed_on','total_amount', 'item')