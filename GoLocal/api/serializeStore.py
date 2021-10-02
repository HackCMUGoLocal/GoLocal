from rest_framework.serializers import ModelSerializer
from .models import Store

class StoreSerializer(ModelSerializer):
    class Meta:
        model = Store
        field = '__all__'