from django import forms

INPUT_CLASS = 'border border-gray-300 rounded-lg text-sm text-gray-900 focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'


class CreateSurvey(forms.Form):  

   date = forms.DateField(widget=forms.TextInput(attrs={'class': INPUT_CLASS, 'type':'date'}))
   topic = forms.CharField(max_length=50, label='Survey Topic', widget=forms.TextInput(attrs={'class': INPUT_CLASS}))
   question =  forms.CharField(widget=forms.Textarea(attrs={"rows":"2", "cols": "25", 'class': INPUT_CLASS})) 
   creator = forms.CharField(max_length=100, label='Creator', widget=forms.TextInput(attrs={'class': INPUT_CLASS}))
   choiceone = forms.CharField(max_length=50, label='Choice One', widget=forms.TextInput(attrs={'class': INPUT_CLASS}))
   choicetwo = forms.CharField(max_length=50, label='Choice Two', widget=forms.TextInput(attrs={'class': INPUT_CLASS}))
   choicethree = forms.CharField(max_length=50, label='Choice Three', widget=forms.TextInput(attrs={'class': INPUT_CLASS}))
   status =  forms.CharField(widget=forms.HiddenInput(), initial='Pending') 

