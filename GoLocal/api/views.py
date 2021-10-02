from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializeStore import StoreSerializer
from .serializeProduct import ProductSerializer
from .models import Store, Product 

@api_view(['GET'])
def getRoutes(request):
  routes = [
    {
      'Endpoint': '\city',
      'method': 'GET',
      'body': None,
      'description': 'Returns local businesses in a city'
    },
    {
      'Endpoint': '\keyword',
      'method': 'GET',
      'body': None,
      'description': 'Returns local businesses from a keyword'
    },
    {
      'Endpoint': '\store',
      'method': 'GET',
      'body': None,
      'description': 'Returns information about a store'
    },
    {
      'Endpoint': '\store',
      'method': 'POST',
      'body': {
        'name': "",
        'location': "",
        'phone': "",
        'website': "",
        'hoursOfOperation': "", 
      },
      'description': 'Creates a new store'
    },
  ]
  return Response(routes)

@api_view(['GET'])
def getStore(request):
  stores = Store.objects.all()
  serializer = StoreSerializer(stores, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def getProduct(request):
  products = Product.objects.all()
  serializer2 = ProductSerializer(products, many=True)
  return Response(serializer2.data)
