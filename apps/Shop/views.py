from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Shop
from .serializers import ShopSerializer


class ShopListView(APIView):

    def get(self, request):
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShopSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ShopDetailView(APIView):

    def get_object(self, pk):
        try:
            return Shop.objects.get(pk=pk)
        except Shop.DoesNotExist:
            return None

    def get(self, request, pk):
        shop = self.get_object(pk)

        if shop is None:
            return Response(
                {"detail": "Магазин не найден"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ShopSerializer(shop)
        return Response(serializer.data)

    def put(self, request, pk):
        shop = self.get_object(pk)

        if shop is None:
            return Response(
                {"detail": "Магазин не найден"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ShopSerializer(shop, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        shop = self.get_object(pk)

        if shop is None:
            return Response(
                {"detail": "Магазин не найден"},
                status=status.HTTP_404_NOT_FOUND
            )

        shop.delete()

        return Response(
            {"detail": "Магазин удалён"},
            status=status.HTTP_204_NO_CONTENT
        )