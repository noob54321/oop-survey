from django import forms
from . import models

class Exam(forms.ModelForm):

	CHOICES = ((1,"Never"),
			   (2,"TEST1"),
			   (3,"KMOT"),
			   (4,"ss"),
			   (5,"dsds"))

	question_1 = forms.ChoiceField(choices = CHOICES, widget = forms.RadioSelect , label = "The Time you always spend reading books")
	question_2 = forms.ChoiceField(choices = CHOICES, widget = forms.RadioSelect , label = "Kamote kamote")
	question_3 = forms.ChoiceField(choices = CHOICES, widget = forms.RadioSelect , label = "FFF")
	class Meta:
		model = models.Personality
		fields = ['question_1','question_2','question_3']