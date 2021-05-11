from rest_framework import serializers
from Django_Project.Application.models import Unit
from Django_Project.Application.models import Lesson
from Django_Project.Application.models import Challenge
from Django_Project.Application.models import UsrAnswers


# Serializers for our different models: 
# Allows us to translate a model instance into Python Native datatypes and
# vice-versa. 
# Used to help us render JSON files going out and 
# to Parse JSON files coming in
class UnitSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Unit
        fields = ['unitid','unitoverview','unittitle']


class LessonSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Lesson
        fields = ['lessonid','unitid','lessonmaterial', 'lessontitle', 'lessondescription']


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Challenge
        fields = ['challengeid','lessonid','challengeoverview', 'filekey', 'unitid']


class UsrAnswerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = UsrAnswers
        fields = ['userid','lessonid','success_state','answer']