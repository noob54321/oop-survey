from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import reverse,render
from . import forms
from . import models

def index(request):
	return render(request, 'exam/personality.html')


def success(request):
	return render(request, 'exam/personality-success.html')

class PersonalityAddView(generic.CreateView):
	model = models.Personality
	form_class = forms.Exam
	template_name = "exam/personality-add.html"

	def get_success_url(self):
		return reverse('exam:success')