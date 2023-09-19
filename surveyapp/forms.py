from django import forms


class CreateSurvey(forms.Form):  
    
   # template_name = "surveys/newsurvey.html"

    date = forms.DateField()
    topic = forms.CharField(max_length=50)
    question = forms.CharField(max_length=100)
    creator = forms.CharField(max_length=100)
    choiceone = forms.CharField(max_length=50)
    choicetwo = forms.CharField(max_length=50)
    choicethree = forms.CharField(max_length=50)
    status =  forms.CharField(widget=forms.HiddenInput(), initial='Pending') 

