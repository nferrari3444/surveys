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
import itertools
from django.contrib import messages
from itertools import chain
from .forms import CreateSurvey

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
    
    print('choicelist', choicelist)
    print('requestmethod', request.method)
    # questionId = Survey.objects.filter(question = question).values_list('id',flat=True).first()

    # question_db = Survey.objects.filter(id = questionId) 
    # newquestion = list(question_db)[0]

    # if Uservotes.objects.filter(question_name= newquestion, username = request.user).exists():
    #     messages.error(request, "User already voted in this Poll")
    #     print('request.path_info',request.path_info)
    #     return HttpResponseRedirect(request.path_info)
    
    if request.method == 'POST':
  #  def post(self, request, *args, **kwargs):

        # print('questionId is', question.id)
        username = request.user
       # question = Survey.objects.filter(question = question)
        questionId = Survey.objects.filter(question = question).values_list('id',flat=True).first()

        print('questionId in querySet' , questionId)

    # idQuestion = list(questionId)[0]
        question_db = Survey.objects.filter(id = questionId)   #.values()
    # questionId = list(questionId)[0]
        # print('choice', choice)
        print('user', request.user)
        # print('questionId', questionId) 
        print('question', list(question_db)[0]) 
        newquestion = list(question_db)[0]
    
        responseexist = Uservotes.objects.filter(question_name= newquestion, username = request.user).exists()
        print(responseexist)

        if Uservotes.objects.filter(question_name= newquestion, username = request.user).exists():
            messages.error(request, "User already voted in this Poll")
            print('request.path_info',request.path_info)
            return HttpResponseRedirect(request.path_info)
        
        else:

            Uservotes.objects.create(username= username, question_name=  newquestion, answer = choice )
            Survey.objects.filter(question=question).update(submissions = F('submissions') + 1 )
            
            Results.objects.update_or_create(question = newquestion, selectedchoice = choice, votes = 1)
        
            return HttpResponseRedirect(request.path_info)
    #raise BadRequest('Invalid request.') #HttpResponseRedirect(request.path_info) #
    

    return redirect('/')  #   return HttpResponse('You should vote for any option or go Home')
    
        #return HttpResponse('Awesome, thanks for voting!')
    # username = request.user
    # print('username', username)
    # print('question',question)

    # if request.method == 'POST':

    #     if Uservotes.objects.filter(question_name=question, username=request.user).exists():
    #         print('es un voter')
    #         messages.info(request, 'User already vote in this Survey!')
    #         messages.error(request,'User already vote in this Survey')

    #     voters = [username.username for username in Uservotes.objects.filter(question_name=question)]
    #     print('voters', voters)
    #     print('request.user', request.user)

    #     if request.user == voters:
    #         print('es un voter')

    #     choice = request.POST.get('choice','choice')
    #     print('choice',choice)
    #     Survey.objects.filter(question=question).update(submissions = F('submissions') + 1 )
        
       
        
    #     if Uservotes.objects.filter(question_name_id=questionId, username=username).exists():
    #          messages.info(request, 'User already vote in this Survey!')
        
    #     else:
    #          Uservotes.objects.create(username= username, question_name=question, answer = choice )
        
    #     if not Results.objects.filter(question=question, selectedchoice=choice).exists():
    #         Results.objects.create(question = question, selectedchoice = choice, votes =1)
            
    #     else:

    #         Results.objects.filter(question=question, selectedchoice=choice).update(votes = F('votes') +1)
           
    # return redirect('/')


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

    print('username', username)
    items = Uservotes.objects.select_related('question').filter(username=username).values()
    votes = Uservotes.objects.select_related('question_name').filter(username=username)  # values().order_by('question_name')
    from django.db.models import F

   # paintings = Uservotes.objects.annotate(name=F('question__name')).all().values()
  
   # question = Uservotes.objects.filter(username=username).values('question').values()
   # question_text = Survey.objects.filter(id= votes).values('question')
   # answers = Uservotes.objects.filter(username=username).values_list(('question', 'answer'), flat=True)
   # questions_id = [vote['question_id'] for vote in votes]
   # answers = [vote['answer'] for vote in votes]
  #  from django.db.models import CharField, Value
   # print(questions_id)
  #  surveyinfo = Survey.objects.filter(pk__in = questions_id).values() #_list('question', 'date','submissions') # , flat=True)
   # surveyinfo_list = list(list(survey) for survey in surveyinfo)      # list(itertools.chain(*surveyinfo))
   # dd = Uservotes.objects.all().annotate(question=Value('question', output_field=CharField()))
   # all = Uservotes.objects.all().values()
   # votes = list(zip(surveyinfo_list,answers))
   # print('username', username)
    print('votes', votes)
    print('items',items)

   # print('paintings', paintings)
   # print('all', all)
   # print('surveyinfo_list', surveyinfo_list)
   # print('surveyinfo', surveyinfo)
    # print('answers',answers)

  #  all = list(chain(surveyinfo, votes))

    context = {'surveyinfo': votes}
    # context.update({'answers':answers})
    print('\n')
    print('all', all)
    return render(request, 'surveys/myvotes.html', context )

def NewSurvey(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
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


            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateSurvey()

    return render(request, "surveys/newsurvey.html", {"form": form})

def Login(request):

    # print('login view')
    # print(request)
    page = 'login'
    # if form.data['first_name'] is None:
    #     print('si')
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
        context = {'page': page}
        return render(request, 'registration/login.html',context)


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

