from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.core.exceptions import PermissionDenied
from .serializers import *

# Create your views here.


class MoveCreateView(CreateAPIView):
    queryset = Move.objects.all()
    serializer_class = MoveSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = User.objects.get(id=self.request.user.id)
        return super().perform_create(serializer.save(owner=user))


class MoveListFilteredView(ListAPIView):
    serializer_class = MoveSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = Move.objects.filter(owner_id=self.request.user.id)
        return qs.order_by("move_date")


class MoveRUDView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = MoveSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.user != self.object.owner:
            raise PermissionDenied("Unauthorized User")
        return super().get(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.user != self.object.owner:
            raise PermissionDenied("Unauthorized User")
        return super().patch(request, *args, **kwargs)

    def get_queryset(self):
        return Move.objects.filter(id=self.kwargs["id"])


class MoveDetailView(ListAPIView):
    serializer_class = MoveSerializer

    def get_queryset(self):
        print("hehuaeh", self.kwargs)
        return Move.objects.filter(id=self.kwargs["pk"])


class ItemCreateView(CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]


class PlaceCreateView(CreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [IsAuthenticated]


class ItemListFilteredView(ListAPIView):
    # change to list only items matching move id
    # just delete and create items when they move
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    queryset = Item.objects.all()

    # def get_queryset(self):
    #     print(f"self, {self}")
    #     print(Item.objects.all())
    #     qs = Item.objects.filter(move_id=self.request.user.id)
    #     print(f"qs, {qs}")
    #     return qs


# class PlaceListFilteredView(ListAPIView):
#     # change to list only places matching move id
#     serializer_class = PlaceSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         qs = Place.objects.filter(owner_id=self.request.user.id)
#         return qs


class ItemRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]


class PlaceRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [IsAuthenticated]
