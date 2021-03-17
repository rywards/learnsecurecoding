# ment to show as example, this script doesn' trun
from Application.models import Unit
from Application.serializers import UnitSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

#Serialization
# Make Unit
unit = Unit(unitid='1', unitoverview='this is a test 1')
unit.save()

#Serialize Unit
serializer = UnitSerializer(unit)

#renderer to JSON
content = JSONRenderer().render(serializer.data)

#Deserialization 
stream = io.BytesIO(content)
data = JSONParser.parse(stream)

serializer = UnitSerializer(data=data)
# can use serializer.is_valid() to check if 
# can use serailizer.validated_data to see dictionary of data

serializer.save()

#we can serialize querysets instead of model instances with many = true flag
# serializer = UnitSerializer(Unit.objects.all(), many=True)
