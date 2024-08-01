from rest_framework import generics
from .serializers import FoodListSerializer
from ..service.db import get_filtered_queryset


class FoodListApiView(generics.ListAPIView):
    serializer_class = FoodListSerializer
    queryset = get_filtered_queryset()
