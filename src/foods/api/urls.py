from django.urls import path
from .views import FoodListApiView

urlpatterns = [
    path('food/', FoodListApiView.as_view()),
]
