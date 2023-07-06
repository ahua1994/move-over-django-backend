from django.urls import path
from .views import *

urlpatterns = [
    path("move/", MoveCreateView.as_view()),
    path("move/<int:id>/", MoveRUDView.as_view()),
    path("mymoves/", MoveListFilteredView.as_view()),
    path("<int:pk>/", MoveDetailView.as_view()),
    path("item/", ItemCreateView.as_view()),
    path("place/", PlaceCreateView.as_view()),
    path("item/all/", ItemListFilteredView.as_view()),
    # path("place/all/", PlaceListFilteredView.as_view()),
    path("item/<int:pk>/", ItemRUDView.as_view()),
    path("place/<int:pk>/", PlaceRUDView.as_view()),
]
