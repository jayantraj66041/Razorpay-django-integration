from django.urls import path
from .views import Home, Details

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path("<int:id>", Details.as_view(), name="details"),
]
