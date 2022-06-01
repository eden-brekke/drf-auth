from rest_framework import generics
from .models import PetPic
from .serializers import PetPicSerializer
from .permissions import IsOwnerOrReadOnly


# Create your views here.
class PetPicList(generics.ListCreateAPIView):
  queryset = PetPic.objects.all()
  serializer_class = PetPicSerializer
  
  
class PetPicDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = PetPic.objects.all()
  serializer_class = PetPicSerializer
  