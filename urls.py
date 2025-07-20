
from django.urls import path
from .views import PlaceFromCoords

urlpatterns = [
    path('get-place/', PlaceFromCoords.as_view()),
]
