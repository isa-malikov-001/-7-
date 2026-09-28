from django.urls import path
from .views import ShopListView, ShopDetailView


urlpatterns = [
    path('shops/', ShopListView.as_view()),
    path('shops/<int:pk>/', ShopDetailView.as_view()),
]