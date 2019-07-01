from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import OtherUserDetails, Item
from rest_framework import authentication, permissions
from api.serializers import ItemSerializer


class ItemViews(APIView):
#     authentication_classes = (authentication.TokenAuthentication,)
#     permission_classes = (permissions.IsAdminUser,)
    """
    List all items, or create a new item.
    """

    def get(self, request, format=None):
        items = Item.objects.all()
        itemsSerializer = ItemSerializer(items, many=True)
        return Response(itemsSerializer.data)
    
    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

