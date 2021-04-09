from solution.models import Operation
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(('GET',))
def get_collection_frequency(request):
    q = Operation.objects.values_list('collection_frequency', flat=True)
    return Response(q)