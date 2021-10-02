from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializeStore import StoreSerializer
from .models import Store

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
def getStores(request):
  stores = Store.objects.all()
  serializer = StoreSerializer(stores, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def getStore(request, pk):
  store = Store.objects.get(id=pk)
  serializer = StoreSerializer(store, many=False)
  return Response(serializer.data)

@api_view(['POST'])
def createStore(request):
  data = request.data
  store = Store.objects.create(
    name = data['name'],
    location = data['location'],
    phone = data['phone'],
    website = data['website'],
    hoursOfOperation = data['hoursOfOperation'],
    category = data['category'],
  )
  serializer = StoreSerializer(store, many=False)
  return Response(serializer.data)

@api_view(['DELETE'])
def deleteStore(request, pk):
  store = Store.objects.get(id=pk)
  store.delete()
  return Response('Store was deleted!')

