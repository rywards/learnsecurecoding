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


"""
    Primary class that handles the view of the challenge-lesson page
"""
class LessonPageView(generics.ListCreateAPIView):
    serializer_class = UsrAnswerSerializer
    queryset = Lesson.objects.all()
    template = './lesson-challenge'

    # Handles GET requests
    def list(self, request, *args, **kwargs):
        pk = kwargs['pk']
        unit_id = kwargs['unit_id']
        if pk != None and unit_id != None:
            lesson_material = Lesson.objects.get(lessonid=pk).lessonmaterial
            challenge = Challenge.objects.get(lessonid=pk)
            challenge_code = challenge.challengeoverview
            challenge_id = challenge.challengeid
            html = pug.render(self.template, {'lesson_material': lesson_material,
                                        'challenge_code': challenge_code,
                                        'lesson_id': pk,
                                        'unit_id':unit_id,
                                        'challenge_id': challenge_id})
            
            return HttpResponse(html)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    

	# Handles POST requests
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


"""
This class handles the View for the unit overview page
"""
class HomePageView(generics.ListAPIView):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()
    template = "./homepage"

    """
    This method is used to make our dictionary of variables to pass to pug.render
    Each key in the dictionary will be 'unit_' + the units id
    Each value will be the unitoverview associated with that unit
    """
    def make_unit_dictionary(self):
        dictionary = {}
        var_base_name = 'unit_'
        current_queryset = self.get_queryset()
        for unit in current_queryset:
            dictionary[var_base_name + unit.unitid] = unit.unitoverview

        return dictionary

    """
    Overriden method from generic view class in order to handle get requests
    """
    def list(self, request, *args, **kwargs):
        html = pug.render(self.template, self.make_unit_dictionary())
        return HttpResponse(html)


"""
This handles the page for the view where the user can choose a lesson from a unit
"""
class ChooseLessonPageView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    template = './unit-overview-temp'


    """
    This method is used to make our dictionary of variables to pass to pug.render
    Each key in the dictionary will be 'lesson_' + the lesson's id
    Each value will be the lesson material associated with that lesson
    """
    def make_lesson_dictionary(self, unitid):
        dictionary = {}
        var_base_name = 'lesson_'
        current_queryset = self.get_queryset().filter(unitid=unitid)
        for lesson in current_queryset:
            dictionary[var_base_name + lesson.lessonid] = lesson.lessonmaterial

        return dictionary



    """
    Overriden Method from the generic class view in order to handle get requests
    """
    def list(self,request, *args, **kwargs):
        pk = kwargs['pk']
        if pk != None: 
            vars = self.make_lesson_dictionary(unitid=pk)
            vars['unit_id'] = pk
            html = pug.render(self.template, vars = vars)
            return HttpResponse(html)

        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
            
            
            


"""Django class based views using generic views pre build by Django REST
ListCreateAPIView: handles get requests for a list of items
RetrieveAPIView: handles get requests for specific items in the queryset
These views are here so we can view Database information without needing
to go to the server directly. We can use these to check database information
in the browser."""
class UnitList(generics.ListAPIView):
    """
    List all units, or create a new unit
    """
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class UnitDetail(generics.RetrieveAPIView):
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


class LessonDetail(generics.RetrieveAPIView):
    """
    Retrieve, update or delete a lesson instance
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer



class ChallengeList(generics.ListAPIView):
    """
    List all Challenges, or create a new challenge
    """
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer


class ChallengeDetail(generics.RetrieveAPIView):
    """
    Retrieve, update or delete a challenge instance
    """
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer


class UsrAnswersList(generics.ListAPIView):
    """
    List all User answers, or create a User Answer
    """
    queryset = UsrAnswers.objects.all()
    serializer_class = UsrAnswerSerializer


class UsrAnswersDetail(generics.RetrieveAPIView):
    """
    Retrieve, update or delete a User answer instance
    """
    queryset = UsrAnswers.objects.all()
    serializer_class = UsrAnswerSerializer