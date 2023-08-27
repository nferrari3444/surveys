from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

from django.views.generic import TemplateView



urlpatterns = [ 

    path('', views.SurveyHome, name='home'),
    path('<int:surveyID>', views.QuestionList, name='surveyoptions'),
    path('choices/<str:question>', views.SurveyResponse, name='choices'),
    path('submissions/', views.Submissions, name='submissions'),
    path('results/<int:questionId>', views.Pollresults, name='results'),
    path('accounts/login/', views.Login, name='login'),
    path('accounts/register/', views.Register, name='register'),
    path('accounts/logout/', views.Logout, name='logout')
  
   
]

urlpatterns += staticfiles_urlpatterns()

