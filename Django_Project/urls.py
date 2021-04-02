"""Django_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework import routers
from Django_Project.Application import views
from django.urls import path, include

router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)



#Wire up our API using automatic URL routing
#Additionally, we include login URLs for the browsable API. 
urlpatterns = [
    path('', views.HomePageView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('Django_Project.Application.urls')),
    path('unit/<int:pk>/lessons/', views.ChooseLessonPageView.as_view()),
    path('unit/<int:unit_id>/lessons/<int:pk>', views.LessonPageView.as_view()),

]
