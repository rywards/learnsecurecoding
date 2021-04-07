# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# Currently Django doesn't support On Update Cascade,
# may need to use django signals for a workaround if needed

class Unit(models.Model):
    unitid = models.CharField(db_column='unitID', primary_key=True, max_length=4)  # Field name made lowercase.
    unitoverview = models.CharField(db_column = 'unitoverview', max_length=3750, blank=True, null=True)
    unittitle = models.CharField(db_column='unitTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'unit'

        
class Lesson(models.Model):
    lessonid = models.CharField(db_column='lessonID', primary_key=True, max_length=4)  # Field name made lowercase.
    unitid = models.ForeignKey('Unit', on_delete= models.CASCADE, db_column='unitID', blank=True, null=True)  # Field name made lowercase.
    lessonmaterial = models.CharField(db_column = 'lessonmaterial', max_length=7500, blank=True, null=True)
    lessontitle = models.CharField(db_column='lessonTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lessondescription = models.CharField(db_column='lessonDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lesson'


class Challenge(models.Model):
    challengeid = models.CharField(db_column='challengeID', primary_key=True, max_length=4)  # Field name made lowercase.
    lessonid = models.ForeignKey('Lesson', on_delete=models.CASCADE, db_column='lessonID', blank=True, null=True)  # Field name made lowercase.
    challengeoverview = models.CharField(db_column = 'challengeoverview', max_length=3750, blank=True, null=True)
    filekey = models.CharField(db_column='fileKey', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'challenge'



class UsrAnswers(models.Model):
    userid = models.AutoField(db_column='userID', primary_key=True)  # Field name made lowercase.
    lessonid = models.ForeignKey(Lesson, on_delete= models.CASCADE, db_column='lessonID', blank=True, null=True)  # Field name made lowercase.
    success_state = models.IntegerField(db_column = 'success_state', blank=True, null=True)
    answer = models.CharField(db_column = 'answer', max_length=7500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usr_answers'
