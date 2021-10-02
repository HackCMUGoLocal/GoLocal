from django.http import JsonResponse

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
  return JsonResponse(routes, safe=False)