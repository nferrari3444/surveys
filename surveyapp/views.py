from django.shortcuts import render
from .models import Choices, Survey, Results   ,   Uservotes
from django.utils import timezone
from django.views.generic import ListView
from django.shortcuts import redirect
from django.db.models import Count, F, Value
from django.db.models import Sum
from django.http import JsonResponse
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.exceptions import BadRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import itertools
import re
from django.conf import settings
from django.contrib import messages
from itertools import chain
from .forms import CreateSurvey
from django.core.mail import send_mail

@login_required
def SurveyHome(request):
    model = Survey
    
    surveys = Survey.objects.all().values()
  
    
    return render(request, 'surveys/home.html', {'surveys':surveys})


def QuestionList(request, surveyID):
    model = Choices
    print(surveyID)
    #options = Choices.objects.all
    #template_name = 'surveys/home.html'

    mainquestion = Survey.objects.filter(id=surveyID)[0]#.values()
    print('mainquestion is', mainquestion)
    options = Choices.objects.filter(question_id=surveyID).values()
    #context_object_name = 'options'

    
    return render(request,              
                'surveys/survey.html',
                {'options': options, 'question': mainquestion, 'surveyID': surveyID})

#@login_required
def SurveyResponse(request, surveyID):
    choice = request.POST.get('choice','choice')
    
    choicelist = request.POST.getlist('choice')
    
    print('choicelist', choicelist)

    print('choice', choice)
    print('requestmethod', request.method)

    print('question is', surveyID)


    if request.method == 'POST':
 
        username = request.user
      
       # questionId = Survey.objects.filter(question = question).values_list('id',flat=True).first()

      

        question_db = Survey.objects.filter(id = surveyID)   #.values()

      
        newquestion = list(question_db)[0]
    
      
        # survey = Survey.objects.filter(id=surveyID)
        # surveyQuestion = Survey.objects.filter(question= surveyID)
        
        # votes =  Results.objects.filter(question = newquestion).filter(selectedchoice=choice).values_list('votes')
        
        # print('votes', votes)


        # print('survey', survey)
        # print('surveyQuestion', surveyQuestion)
        # print('newquestion', newquestion)

        if Uservotes.objects.filter(question_name= newquestion, username = request.user).exists():
            messages.error(request, "User already voted in this Poll", extra_tags='survey_response')
            print('request.path_info',request.path_info)
            return redirect('/%s' % surveyID )
        
        else:

            Uservotes.objects.create(username= username, question_name=  newquestion, answer = choice )
            #Survey.objects.filter(question= question_db).update(submissions = F('submissions') + 1 )
            Survey.objects.filter(id=surveyID).update(submissions = F('submissions') + 1 )
            
            if not Results.objects.filter(question= newquestion, selectedchoice=choice).exists():
                Results.objects.create(question = newquestion, selectedchoice = choice, votes =1)

            else:

                Results.objects.filter(question= newquestion, selectedchoice=choice).update(votes = F('votes') +1)
          
            #Results.objects.update_or_create(question = newquestion, selectedchoice = choice, votes =  1)
        
        return HttpResponseRedirect(request.path_info)
   
    

    return redirect('/')  #   return HttpResponse('You should vote for any option or go Home')
    
  

def Submissions(request):
 
    polls = Survey.objects.all().values()
    print('result is', polls)
   # print('resultpolss is', resultspolls)
    context = {'polls': polls}
    return render(request, 'surveys/submissions.html', context)

def Pollresults(request, questionId):



    results = Results.objects.all()
    print('questionId', questionId)

    polldata = Results.objects.filter(question = questionId ).values("selectedchoice").annotate(votes=Sum('votes')).values()

    question = Survey.objects.filter(id = questionId ).values("question").values()
    print('pollData', polldata)
    for item in question:
        title = item['question']

    print('question is:', title)

   # resultspolls = results.values('question').annotate(votes=Sum('votes'))
    
    
    #print('result is', results)
   # print('resultpolss is', resultspolls)
    context = {'polldata': polldata}

    return JsonResponse({'pollInfo': list(polldata), 'question': title}, safe=False)
    #return render(request, 'surveys/results.html', context)

def Myvotes(request, username):

    user = User.objects.filter(username=username)
  #  .select_related('sensor') 
    print('user', user)
    print('username', username)

    username = re.sub('[^a-zA-Z]+', ' ', username)
    print('clean username', username)


    items = Uservotes.objects.select_related('question').filter(username=username).values()
    votes = Uservotes.objects.select_related('question_name').filter(username=username)  # values().order_by('question_name')
   

  
    print('votes', votes)
    print('items',items)

    context = {'surveyinfo': votes}
    # context.update({'answers':answers})
    print('\n')
    print('all', all)
    return render(request, 'surveys/myvotes.html', context )

def NewSurvey(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        userId = request.user.id
        user = User.objects.get(id=userId)
        user_email = user.email

        print('user',user_email)
        # create a form instance and populate it with data from the request:
        form = CreateSurvey(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            question = form.cleaned_data['question']
            choiceone = form.cleaned_data['choiceone']
            choicetwo = form.cleaned_data['choicetwo']
            choicethree = form.cleaned_data['choicethree']


            date = form.cleaned_data['date']
            topic = form.cleaned_data['topic']

            creator = form.cleaned_data['creator']

            survey = Survey(date= date, topic= topic, question= question, creator= creator)
            survey.save()

            survey_id = Survey.objects.filter(question = question).values_list('id',flat=True).first() 
            
            instance = Survey.objects.get(pk=survey_id)
            choices = Choices(question= instance, choice_1 = choiceone, choice_2 = choicetwo, choice_3 = choicethree)
            choices.save()

            send_mail(
                subject = 'New Survey Created',
                message = 'A new survey was created. Check the admin Panel to approve or reject it',
                from_email = settings.EMAIL_HOST_USER,
                recipient_list=['nferrari3444@gmail.com'],
                fail_silently=False,
                auth_user=None,
                auth_password=None,
                connection=None,
                html_message=None
            )

            messages.info(request, 'Survey was created with success and is waiting for approval', extra_tags='create_survey')
            # return render(request, 'registration/login.html')
            # redirect to a new URL:
            return HttpResponseRedirect("/createsurvey")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateSurvey()

    return render(request, "surveys/newsurvey.html", {"form": form})

def Login(request):

    page = 'login'
    
    if request.method == 'POST':

        email = request.POST.get('email','email')
        
        try:
            validate_email(email)
        except ValidationError as e:
            print("bad email, details:", e)
            messages.error(request, 'Email should contain @', extra_tags='login')
            return render(request, 'registration/login.html')

        username = User.objects.filter(email=email).values_list('username', flat=True)
        password = request.POST.get('password','password')
    
        print('usernameLength' , len(username))
        print('passwordLength', len(password))

        print('username' , username)
        print('password', password)

        if len(username) == 0 | len(password) == 0:
            messages.error(request, "Should add a user Name and password to Log In", extra_tags='login')
            return render(request, 'registration/login.html')
        
        
        print('username' , username)
        username = username[0]
        # user_ = self.cleaned_data.get('email')
        

       # password = request.POST['password']

        print(username)

        user = authenticate(request, username =username,  password=password)

        print('user',user)
        if user is not None:
            #if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return redirect('/')
        #else:
            # Return a 'disabled account' error message
            ...
        else:
        # Return an 'invalid login' error message.
            print('user not exist')
            messages.info(request, 'User does not exist. Please Sign Up first!')
            return render(request, 'registration/login.html')

        userLoggedIn = Users.objects.filter(username = user)

        users = Users.objects.all().values()
        print(users, 'users' )

        #Users.save(user,  password)
        print('user is ', user)

        
        # print('user_ is ', user_)
   

    else:
        context = {'page': page}
        return render(request, 'registration/login.html',context)


def Register(request):

    if request.method == 'POST':


        username = request.POST.get('username','username')    
        email = request.POST.get('email','email')

 
        
        try:
            validate_email(email)
        except ValidationError as e:
            print("bad email, details:", e)
            messages.error(request, 'Email should contain @', extra_tags='register')
            return render(request, 'registration/register.html')
        
        # user_ = self.cleaned_data.get('email')
        password = request.POST.get('password','password')

        newUser = User.objects.create_user(username=username,  email= email  , password=password  )

        newUser.save()

        return render(request, 'registration/login.html')
    
    else:

        return render(request, 'registration/register.html')
    

def Logout(request):

    logout(request)
    
    return redirect('/')

