from rest_framework.generics import CreateAPIView

from .serializers import *


class ContactCreateAPIView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

