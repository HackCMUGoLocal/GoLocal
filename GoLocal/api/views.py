from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializeStore import StoreSerializer
from django.views.decorators.csrf import csrf_exempt
from .models import Store

@api_view(['GET'])
def getRoutes(request):
  routes = [
    {
      'Endpoint': '\stores',
      'method': 'GET',
      'body': None,
      'description': 'Returns local businesses'
    },
    {
      'Endpoint': '\store\<int:pk>',
      'method': 'GET',
      'body': None,
      'description': 'Returns local businesses where id=pk'
    },
    {
      'Endpoint': '\store\create',
      'method': 'POST',
      'body': {
        'name': "",
        'location': "",
        'phone': "",
        'website': "",
        'hoursOfOperation':"",
        'category': "",
      },
      'description': 'Creates a new store with given body data'
    },
    {
      'Endpoint': '\store\<int:pk>',
      'method': 'DELETE',
      'body': None,
      'description': 'Deletes store with id=pk'
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

