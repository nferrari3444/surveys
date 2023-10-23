from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

from django.views.generic import TemplateView



urlpatterns = [ 

    path('', views.SurveyHome, name='home'),
    path('<int:surveyID>', views.QuestionList, name='surveyoptions'),
    path('choices/<int:surveyID>', views.SurveyResponse, name='choices'),
    path('submissions/', views.Submissions, name='submissions'),
    path('results/<int:questionId>', views.Pollresults, name='results'),
    path('myvotes/<str:username>', views.Myvotes, name='myvotes'),
     path('createsurvey/', views.NewSurvey, name='newsurvey'),
    path('accounts/login/', views.Login, name='login'),
    path('accounts/register/', views.Register, name='register'),
    path('accounts/logout/', views.Logout, name='logout'),
  
    path('accounts/', include('allauth.urls')),
   
]

urlpatterns += staticfiles_urlpatterns()

