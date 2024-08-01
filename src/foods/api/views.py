from rest_framework import generics
from .serializers import FoodListSerializer
from ..models import FoodCategory, Food
from django.db.models import Prefetch


class FoodListApiView(generics.ListAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        published_foods = Food.objects.filter(is_publish=True)
        return FoodCategory.objects.prefetch_related(Prefetch('food', queryset=published_foods)).filter(
            food__is_publish=True).distinct()
