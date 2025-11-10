from django.urls import path
from .views import *

urlpatterns = [
    path("api/menu-categories/", MenuCategoryListAPIView.as_view(), name = "menu-category-list")
]