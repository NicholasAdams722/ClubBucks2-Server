"""View module for handling requests for item data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from clubbucksapi.models import Item, ItemType, Transaction
from django.contrib.auth.models import User
from rest_framework.decorators import action

class ItemView(ViewSet):
    """Honey Rae API items view"""

    def list(self, request):
        """Handle GET requests to get all items

        Returns:
            Response -- JSON serialized list of items
        """

        # user = User.objects.get(id= request.auth.user.id)
        # items = Item.objects.get(user_id=user.id)
        items = Item.objects.all()
        serialized = ItemSerializer(items, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single item

        Returns:
            Response -- JSON serialized item record
        """

        item = Item.objects.get(pk=pk)
        serialized = ItemSerializer(item)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    # complete and test create function for item

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized item instance
        """

        #Foreign keys on a new  object.  These will be the fields in the item form
        item_type = ItemType.objects.get(pk=request.data["item_type"])

        item = Item.objects.create(
            name=request.data["name"],
            description=request.data["description"],
            price=request.data["price"],
            image=request.data["image"],
            item_type = item_type,
            quantity = request.data["quantity"]
        )
        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # complete and test an update function for an item

    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        item = Item.objects.get(pk=pk)
        item.name = request.data["name"]
        item.description = request.data["description"]
        item.price = request.data["price"]
        item.image = request.data["image"]
        item_type = ItemType.objects.get(pk=request.data["item_type"])
        item.item_type = item_type
        item.quantity = request.data["quantity"]
        item.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    # complete and test a destroy function for an item

    def destroy(self, request, pk):
        item = Item.objects.get(pk=pk)
        item.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=True)
    def add_to_order(self, request, pk):
        """Add a product to the current users open order"""
        try:
            item = Item.objects.get(pk=pk)
            order, _ = Transaction.objects.get_or_create(
                user=request.auth.user, completed_on=None, payment_type=None)
            order.items.add(item)
            return Response({'message': 'product added'}, status=status.HTTP_201_CREATED)
        except Item.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


class ItemSerializer(serializers.ModelSerializer):
    """JSON serializer for items"""
    class Meta:
        model = Item
        fields = ('id', 'name', 'item_type', 'description', 'price', 'image', 'quantity')