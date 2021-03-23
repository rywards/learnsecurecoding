from django.http import HttpResponse
from Django_Project.Application.models import Unit, Lesson
from Django_Project.Application.models import Challenge, UsrAnswers
from Django_Project.Application.serializers import UnitSerializer, LessonSerializer
from Django_Project.Application.serializers import ChallengeSerializer, UsrAnswerSerializer
import Django_Project.Application.pug as pug
from rest_framework import generics

def test(request):
    html = pug.render('./test.pug', {'var1': 'bar'})
    return HttpResponse(html)

def challenge(request):
    html = pug.render('./lesson-challenge', {'var1': 'bar'})
    return HttpResponse(html)

# unitoverview and homepage added by Ryan
def unitoverview(request):
    html = pug.render('./unit-overview-temp', {'var1': 'bar'})
    return HttpResponse(html)

def homepage(request):
    html = pug.render('./homepage', {'var1': 'bar'})
    return HttpResponse(html)


#Django class based views using APIView Wrapper class
#ListCreateAPIView handles: get and post requests
#RetrieveUpdateDestryAPIView handles: get, put, and delete requests
class UnitList(generics.ListCreateAPIView):
    """
    List all units, or create a new unit
    """
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class UnitDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a Unit instance
    """
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer



class LessonList(generics.ListCreateAPIView):
    """
    List all lessons, or create a new lesson
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a lesson instance
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer



class ChallengeList(generics.ListCreateAPIView):
    """
    List all Challenges, or create a new challenge
    """
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer


class ChallengeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a challenge instance
    """
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer


class UsrAnswersList(generics.ListCreateAPIView):
    """
    List all User answers, or create a User Answer
    """
    queryset = UsrAnswers.objects.all()
    serializer_class = UsrAnswerSerializer


class UsrAnswersDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a User answer instance
    """
    queryset = UsrAnswers.objects.all()
    serializer_class = UsrAnswerSerializer