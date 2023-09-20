from django import forms


class CreateSurvey(forms.Form):  
    
   # template_name = "surveys/newsurvey.html"

   
   date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}))
   topic = forms.CharField(max_length=50, label='Survey Topic')
   question =  forms.CharField(widget=forms.Textarea(attrs={"rows":"2", "cols": "25"})) 
   creator = forms.CharField(max_length=100, label='Creator')
   choiceone = forms.CharField(max_length=50, label='Choice One')
   choicetwo = forms.CharField(max_length=50, label='Choice Two')
   choicethree = forms.CharField(max_length=50, label='Choice Three')
   status =  forms.CharField(widget=forms.HiddenInput(), initial='Pending') 

