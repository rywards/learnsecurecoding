from django.http import HttpResponse
from Django_Project.Application.models import Unit, Lesson
from Django_Project.Application.models import Challenge, UsrAnswers
from Django_Project.Application.serializers import UnitSerializer, LessonSerializer
from Django_Project.Application.serializers import ChallengeSerializer, UsrAnswerSerializer
import Django_Project.Application.pug as pug
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

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



class LessonPageView(generics.ListCreateAPIView):
    """
    Primary class that handles the view of the challenge-lesson page
    """
    serializer_class = UsrAnswerSerializer
    queryset = Lesson.objects.all()

    
    def list(self, request, *args, **kwargs):
        template = './lesson-challenge'
        pk = kwargs['pk']
        if pk != None:
            lesson_material = Lesson.objects.get(lessonid=pk).lessonmaterial
            challenge_code = Challenge.objects.get(lessonid=pk).challengeoverview
            html = pug.render(template, {'lesson_material': lesson_material,
                                        'challenge_code': challenge_code,
                                        'lessonid': pk})
            
            return HttpResponse(html)
    


    def create(self, request, *args, **kwargs):
        data = {}
        data['answer'] = request.data['code']
        data['lessonid'] = request.data['lesson_id']
        data['success_state'] = 0
        serializer = UsrAnswerSerializer(data = data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    






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