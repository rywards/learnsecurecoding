from django.urls import path
from Django_Project.Application import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('units/', views.UnitList.as_view()),
    path('units/<int:pk>/', views.UnitDetail.as_view()),
    path('lessons_details/', views.LessonList.as_view()),
    path('lessons_details/<int:pk>/', views.LessonDetail.as_view()),
    path('challenges/', views.ChallengeList.as_view()),
    path('challenges/<int:pk>/', views.ChallengeDetail.as_view()),
    path('user_answers/', views.UsrAnswersList.as_view()),
    path('user_answers/<int:pk>/', views.UsrAnswersDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)