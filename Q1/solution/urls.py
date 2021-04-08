from django.urls import path
from solution.views import last_points


urlpatterns = [
    path('last-points/', last_points, name="last-points"),
]
