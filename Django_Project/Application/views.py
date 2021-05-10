from django.http import HttpResponse
from Django_Project.Application.models import Unit, Lesson
from Django_Project.Application.models import Challenge, UsrAnswers
from Django_Project.Application.serializers import UnitSerializer, LessonSerializer
from Django_Project.Application.serializers import ChallengeSerializer, UsrAnswerSerializer
import Django_Project.Application.pug as pug
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from Django_Project.Application.cwe_checker import RunChecker
from markdown2 import Markdown

markdowner = Markdown(extras=["fenced-code-blocks"])

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


	#Continuation of workaround found in 'lesson-challenge.pug'.
	def get_correct_lesson_id(self, unit_id, lesson_id):

		tutorial_ids = [7,8]
		tut_unit_id = 0
		tutorial_id_offset = 6

		if unit_id == tut_unit_id:
			for tutorial_id in tutorial_ids:
				if lesson_id == tutorial_id:
					#if tutorial unit and lesson_id already equals a tutorial_id, return that id
					return lesson_id
		
			#if tutorial unit and not already a tutorial id, add the offset and return
			#in this case the only numbers that could appear here is 1 or 2
			return lesson_id + tutorial_id_offset
			
		#if not tutorial unit, return the initial lesson_id
		return lesson_id




	# Handles GET requests
	def list(self, request, *args, **kwargs):
		pk = kwargs['pk']
		unit_id = kwargs['unit_id']
		if pk != None and unit_id != None:
			
			pk = self.get_correct_lesson_id(unit_id,pk)

			lesson = Lesson.objects.get(lessonid = pk, unitid = unit_id)
			numLessons = len(self.get_queryset())
			lesson_material = lesson.lessonmaterial
			lesson_title = lesson.lessontitle
			challenge = Challenge.objects.get(lessonid=pk)
			challenge_code = challenge.challengeoverview
			challenge_id = challenge.challengeid
			html = pug.render(self.template, {'lesson_material': markdowner.convert(lesson_material),
										'challenge_code': challenge_code,
										'lesson_id': pk,
										'unit_id':unit_id,
										'challenge_id': challenge_id,
										'lesson_title': lesson_title,
										'num_Lessons': numLessons,
										'section': 'tutorials' if unit_id == 0 else 'lessons'})
			
			return HttpResponse(html)
		return Response("Error", status= status.HTTP_400_BAD_REQUEST)
	

	# Handles POST requests
	def create(self, request, *args, **kwargs):
		
		answer = request.data['code']
		lesson_id = request.data['lesson_id']
		file_key = Challenge.objects.get(lessonid=lesson_id).filekey
		lesson_title = Lesson.objects.get(lessonid=lesson_id).lessontitle
		
		next_id = str(int(lesson_id) + 1)
		next_title = ''
		try:
			next_title = Lesson.objects.get(lessonid = next_id).lessontitle
		except Exception as e:
			print(e)

		success_state, message = RunChecker(file_key, answer, lesson_title, next_title)
			

		data = {}
		data['answer'] = answer
		data['lessonID'] = lesson_id
		data['success_state'] = 1 if success_state else 0
		serializer = UsrAnswerSerializer(data = data)
		if serializer.is_valid(): 
			serializer.save()
			copy_data = serializer.data
			copy_data['message'] = message
			return Response(copy_data, status=status.HTTP_201_CREATED)
		else:
			print(serializer.errors)
		return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


"""
This class handles the View for the unit overview page
"""
class HomePageView(generics.ListAPIView):
	serializer_class = UnitSerializer
	queryset = Unit.objects.all()
	template = "./homepage"

	"""
	This method is used to make our dictionary of variables to pass to pug.render.
	keys in the dictionary with the form <'unit_' + the units id> will have a value of the unit overview.
	keys in the dictionary with the form <'unit_' + the units id + '_title'> will have a value of the title of the Unit.
	"""
	def make_unit_dictionary(self):
		dictionary = {}
		var_base_name = 'unit_'
		title_var_ending = '_title'
		current_queryset = self.get_queryset()
		for unit in current_queryset:
			dictionary[var_base_name + unit.unitid] = unit.unitoverview
			dictionary[var_base_name + unit.unitid + title_var_ending] = unit.unittitle


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
	This method is used to make our dictionary of variables to pass to pug.render.
	keys in the dictionary with the form <'lesson_' + the lessons id> will have a value of the lesson description.
	keys in the dictionary with the form <'lesson_' + the lessons id + '_title'> will have a value of the title of the lesson.
	Also adds a variable for how many lessons are in the unit
	"""
	def make_lesson_dictionary(self, unitid):
		dictionary = {}
		current_queryset = self.get_queryset().filter(unitid=unitid)
		descriptions = []
		titles = []

		for lesson in current_queryset:
			descriptions.append(lesson.lessondescription)
			titles.append(lesson.lessontitle)

		dictionary['section'] = 'tutorials' if unitid == 0 else 'lessons'
		dictionary['descriptions'] = descriptions
		dictionary['titles'] = titles
		dictionary['numLessons'] = len(current_queryset)

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

		return Response("Error", status= status.HTTP_400_BAD_REQUEST)
			
			
			


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