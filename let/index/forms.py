from django import forms
from . import models


class StatisticForm(forms.ModelForm):
	CHOICES_A = ((1,"Little to None"),
			   (2,"1-2 Days"),
			   (3,"2-3 Days"),
			   (4,"3-4 Days"),
			   (5,"Almost everyday"),)

	CHOICES_B = ((1,"4 Hours or Less"),
			   (2,"4-5 Hours"),
			   (3,"5-6 Hours"),
			   (4,"6-8 Hours"),
			   (5,"8+ Hours"),)

	CHOICES_C = ((1,"You Often Skip Studying"),
			   (2,"You feel like you don't need to study"),
			   (3,"You study when you need to"),
			   (4,"Puts it in a priority"),
			   (5,"Diligently Uphold a Proper Study Routine"),)

			   (4,"Often"),
			   (5, "Always"))


	CHOICES = ((1,"Never"),
			   (2,"Rarely"),
			   (3,"Sometimes"),
			   (4,"Often"),
			   (5, "Always"))

	CHOICES_1 = ((1,"Significantly Negative Impact"),
			   (2,"Negative Impact"),
			   (3,"Neutral/No Impact"),
			   (4,"Positive Impact"),
			   (5, "Significant Positive Impact"))

	CHOICES_2 = ((1,"Strong Disagree"),
			   (2,"Disagree"),
			   (3,"Neutral"),
			   (4,"Agree"),
			   (5, "Strongly Agree"))

	CHOICES_2REV = ( 			 
			   (5,"Strong Disagree"),
			   (4,"Disagree"),
			   (3,"Neutral"),
			   (2,"Agree"),
			   (1,"Strongly Agree"),
)

	CHOICES_4 = ((1,"2 or more of mentioned above"),
			   (2,"Train/Bus"),
			   (3,"Public Utiliy Vehicle"),
			   (4,"Personal Car"),
			   (5, "Walking because it's near"))

	CHOICES_5 = ((5,"5 - 15 mins"),
			   (4,"15 - 30 mins"),
			   (3,"30 mins - 45 Mins"),
			   (2,"45 Mins - 1 Hour"),
			   (1, "More than 1 Hour"))

	CHOICES_6 = ((5,"Less than 10 mins"),
			   (4,"10 - 20 mins"),
			   (3,"20 mins - 35 Mins"),
			   (2,"35 Mins - 50 Mins"),
			   (1, "More than 50 Mins"))

	CHOICES_7 = ((1,"Does not affect me at all"),
			   (2,"Barely affects me"),
			   (3,"Slightly Affects me"),
			   (4,"Affects me "),
			   (5, "Strongly Affects me"))

	CHOICES_8 = ((5,"Rarely"),
			   (4,"Occasionally"),
			   (3,"Sometimes"),
			   (2,"Often"),
			   (1, "Always"))

	#Personal
	f1 = forms.ChoiceField(label="In a week, how many days do you schedule a study session?", choices = CHOICES_A, widget=forms.RadioSelect)
	f2 = forms.ChoiceField(label="How long do you estimate your time of sleep attained per school day?", choices = CHOICES_B, widget=forms.RadioSelect)
	f3 = forms.ChoiceField(label="How would you rate yourself in according with your study habit?", choices = CHOICES, widget=forms.RadioSelect)
	f4 = forms.ChoiceField(label="How often were you in the Honor Roll since Elementary? (Any ranking)", choices = CHOICES, widget=forms.RadioSelect)
	f5 = forms.ChoiceField(label="Do you maintain a healthy work-life balance?", choices = CHOICES, widget=forms.RadioSelect)

	#Family
	f6 = forms.ChoiceField(label="What kind of impact does your overall family bring to your life?", choices = CHOICES_1, widget=forms.RadioSelect)
	f7 = forms.ChoiceField(label="What kind of impact does your parents bring to your life?", choices = CHOICES_1, widget=forms.RadioSelect)
	f8 = forms.ChoiceField(label="Do you consider your family as a source of inspiration to work hard?", choices = CHOICES_2, widget=forms.RadioSelect)
	f9 = forms.ChoiceField(label="Does your family pressure you in a negative way? *", choices = CHOICES_2REV, widget=forms.RadioSelect)
	f10 = forms.ChoiceField(label="Is your family considered a hindrance to your progress in the academe?*", choices = CHOICES_2REV, widget=forms.RadioSelect)

	#Peer
	f11 = forms.ChoiceField(label="Does your peer group have a positive influence that impacts your study habits?", choices = CHOICES_1, widget=forms.RadioSelect)
	f12 = forms.ChoiceField(label="Does your peer group often study together?", choices = CHOICES, widget=forms.RadioSelect)
	f13 = forms.ChoiceField(label="Does your peer group have the same convivtion in studying as you do?", choices = CHOICES, widget=forms.RadioSelect)
	f14 = forms.ChoiceField(label="Does your peer group also do well in academics?", choices = CHOICES, widget=forms.RadioSelect)
	f15 = forms.ChoiceField(label="Does your peer group often engage in extra curricular activites that are positively beneficial?", choices = CHOICES, widget=forms.RadioSelect)

	#School
	f16 = forms.ChoiceField(label="Does the school provide developmental seminars to enchance student skills?", choices = CHOICES, widget=forms.RadioSelect)
	f17 = forms.ChoiceField(label="Does the school maintain top quality curriculums aimed to target critical skills in courses?", choices = CHOICES, widget=forms.RadioSelect)
	f18 = forms.ChoiceField(label="Does the school provide enough material to cater to students' academic needs?", choices = CHOICES, widget=forms.RadioSelect)
	f19 = forms.ChoiceField(label="Does the school have a flxeible administration that handles the flow of the academe well?", choices = CHOICES, widget=forms.RadioSelect)
	f20 = forms.ChoiceField(label="Does the School constantly undergo development of the academe to imrpove education quality?", choices = CHOICES, widget=forms.RadioSelect)

	#Traffic Daw To
	f21 = forms.ChoiceField(label="What is your most frequent mode of transport in going to school?", choices = CHOICES_4, widget=forms.RadioSelect)
	f22 = forms.ChoiceField(label="How long is your travel time to school? (Including traffic)", choices = CHOICES_5, widget=forms.RadioSelect)
	f23 = forms.ChoiceField(label="How long do you get stuck in traffic", choices = CHOICES_6, widget=forms.RadioSelect)
	f24 = forms.ChoiceField(label="Does traffic affect you in any way when it comes to studying? (Fatigue, mood, etc.)", choices = CHOICES_7, widget=forms.RadioSelect)
	f25 = forms.ChoiceField(label="How often do you find yourself stuck in traffic?", choices = CHOICES_8, widget=forms.RadioSelect)

	#name = forms.ChoiceField(choices = CHOICES)
	class Meta:
		model = models.Statistic
		exclude = ('total','over','o1','o2','o3','o4','o5','state')

	def __init__(self, *args, **kwargs):
		super(StatisticForm, self).__init__(*args, **kwargs)
