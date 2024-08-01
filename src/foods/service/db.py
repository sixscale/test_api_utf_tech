from ..models import FoodCategory, Food
from django.db.models import Prefetch


def get_filtered_queryset():
    published_foods = Food.objects.filter(is_publish=True)
    queryset = FoodCategory.objects.prefetch_related(Prefetch('food', queryset=published_foods)).filter(
        food__is_publish=True).distinct()
    return queryset
