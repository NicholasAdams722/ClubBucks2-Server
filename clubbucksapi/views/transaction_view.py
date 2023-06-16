"""View module for handling requests for transaction data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from clubbucksapi.models import Transaction


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


class TransactionSerializer(serializers.ModelSerializer):
    """JSON serializer for transactions"""
    class Meta:
        model = Transaction
        fields = ('id', 'user', 'created_on', 'completed_on','total_amount')