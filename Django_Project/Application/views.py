from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from Django_Project.Application.models import Unit
from Django_Project.Application.serializers import UnitSerializer
import Django_Project.Application.pug as pug

def test(request):
    html = pug.render('./test.pug', {'var1': 'bar'})
    return HttpResponse(html)

def challenge(request):
    html = pug.render('./lesson-challenge', {'var1': 'bar'})
    return HttpResponse(html)


#Regular Django Views
@csrf_exempt
def unit_list(request):
    """
    List all Units, or create a new Unit
    """
    if request.method == "GET":
        units = Unit.objects.all()
        serializer = UnitSerializer(units, many = True)
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser.parse(request)
        serializer = UnitSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)

@csrf_exempt 
def unit_detail(request, pk):
    """
    Retrieve, update or delete a code snippet
    """
    try: 
        unit = Unit.objects.get(pk=pk)

    except Unit.DoesNotExist: 
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = UnitSerializer(unit)
        return JsonResponse(serializer.data)

    
    if request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = UnitSerializer(unit, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == "DELETE":
        unit.delete()
        return HttpResponse(status=204)