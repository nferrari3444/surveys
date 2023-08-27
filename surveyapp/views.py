from django.shortcuts import render
from .models import Choices, Survey, Results, Users
from django.utils import timezone
from django.views.generic import ListView
from django.shortcuts import redirect
from django.db.models import Count, F, Value
from django.db.models import Sum
from django.http import JsonResponse
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.contrib import messages


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
                {'options': options, 'question': mainquestion})

#@login_required
def SurveyResponse(request, question):
    choice = request.POST.get('choice','choice')
    
    choicelist = request.POST.getlist('choice')

    #print('post', request.POST)
    
    question = Survey.objects.get(question=question)#.values()
    questionId = question.id
    #result = Results.objects.get(question_id=questionId)
    #print('result', result)
    #place = Places.objects.get(name='kansas')
    #print(place.id)
    print('questionId is', questionId) 
    print('question is', question)
    #entry = Results.objects.get(question=question)
    #print('entry',entry)
    if request.method == 'POST':
        choice = request.POST.get('choice','choice')
        print('choice',choice)
        Survey.objects.filter(question=question).update(submissions = F('submissions') + 1 )

        if not Results.objects.filter(question=question, selectedchoice=choice).exists():
            Results.objects.create(question = question, selectedchoice = choice, votes =1)
        
        else:

            Results.objects.filter(question=question, selectedchoice=choice).update(votes = F('votes') +1)
        #print('dd', dd)
        #newvote = Results(question=question, selectedchoice=choice, vote=1)
        #dd.save()
    
    #print(choicelist)
    #print('choice is {}'.format(choice))
    return redirect('/')



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


def Login(request):

    # print('login view')
    # print(request)

    if request.method == 'POST':

        email = request.POST.get('email','email')

        #email = request.POST['email']
        
        username = User.objects.filter(email=email).values_list('username', flat=True)

        print('username' , username)
        username = username[0]
        # user_ = self.cleaned_data.get('email')
        password = request.POST.get('password','password')

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

        return render(request, 'registration/login.html')


def Register(request):

    if request.method == 'POST':

        username = request.POST.get('username','username')    
        email = request.POST.get('email','email')

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

