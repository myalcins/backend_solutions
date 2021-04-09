from django.urls import path
from solution.views import get_collection_frequency

urlpatterns = [
    path('collection-frequency/', get_collection_frequency, name="collection-frequency")
]