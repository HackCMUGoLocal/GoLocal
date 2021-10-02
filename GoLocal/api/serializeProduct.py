from rest_framework.serializers import ModelSerializer
from .models import Product

class StoreSerializer(ModelSerializer):
    class Meta:
        model = Product
        field = '__all__'