from rest_framework.serializers import ModelSerializer
from .models import *

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"