from django.db import models

#Currently Django doesn't support On Update Cascade,
#may need to use django signals for a workaround if needed


# Create your models here.
class Unit(models.Model):
    unitID = models.CharField(max_length=4, primary_key=True)
    unitOverview = models.CharField(max_length=3750,)

    class Meta: 
        ordering = ['unitId']


class Lesson(models.Model):
    lessonID = models.CharField(max_length=4, primary_key=True)
    lesson_material = models.CharField(max_length=7500)
    unitID = models.ForeignKey(Unit, on_delete= models.CASCADE)

    class Meta: 
        ordering = ['lessonID']



class Challenge(models.Model):
    challengeID = models.CharField(max_length=4, primary_key=True)
    challenge_overview = models.CharField(max_length=3750)
    lessonId = models.ForeignKey(Lesson, on_delete= models.CASCADE)

    class Meta: 
        ordering = ['challengeID']


class User_Answers(models.Model):
    userID = models.CharField(max_length=9, primary_key= True)
    success_state = models.SmallIntegerField()
    answer = models.CharField(max_length= 7500)
    lessonId = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    class Meta: 
        ordering = ['userID']