from django.shortcuts import render,reverse,  get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.views import generic
from rest_framework.views import APIView
from rest_framework.response import Response
from . import forms
from . import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
def index(request):
	return render(request, 'index/p-ind.html')

class AddView(generic.CreateView):
	form_class = forms.StatisticForm
	model = models.Statistic
	template_name = 'index/p-add.html'

	def form_valid(self, form):
		f = form.save(commit=False)

		o1 = f.f1 + f.f2 + f.f3 + f.f4 + f.f5
		o2 = f.f6 + f.f7 + f.f8 + f.f9 + f.f10
		o3 = f.f11 + f.f12 + f.f13 + f.f14 + f.f15
		o4 = f.f16 + f.f17 + f.f18 + f.f19 + f.f20
		o5 = f.f21 + f.f22 + f.f23 + f.f24 + f.f25

		f.total = o1 + o2 + o3 + o4 + o5
		f.over = f.total / models.Statistic.Max()
		f.o1 = o1
		f.o2 = o2
		f.o3 = o3
		f.o4 = o4
		f.o5 = o5

		f.save()
		return super(AddView,self).form_valid(form)

	def get_success_url(self):
		return reverse('index:ind-view', kwargs = {'pk':self.object.pk})

	# def get_form_kwargs(self, *args, **kwargs):
	# 	kwargs = super(AddView, self).get_form_kwargs(**kwargs)
	# 	return kwargs


class SuccessView(generic.DetailView):
	model = models.Statistic
	template_name = 'index/p-succ.html'
	context_object_name = 'stats'

	# def get_object(self):
	# 	return get_object_or_404(models.Statistic, pk=self.kwargs.get('pk'))

	def get_context_data(self, **kwargs):
		obj = models.Statistic.objects.get(pk = self.kwargs.get('pk'))
		context = super(SuccessView, self).get_context_data(**kwargs)
		context.update({'call' : obj.Calls(),
						'percentage' : obj.Percentage(),
						'overall1' : obj.O1(),
						'overall2' : obj.O2(),
						'overall3' : obj.O3(),
						'overall4' : obj.O4(),
						'overall5' : obj.O5(),
						'total' : obj.TotalO(),
						'average' : obj.TotalO() / 5 })

		return context

def get_data(request, *args, **kwargs):
	data = {
		'sales':100,
		'customers':10,
	}
	return JsonResponse(data)

class ChartData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None, **kwargs):
    	labels = ['Personal Factor', 'Family Factor', 'Peer Factor ', 'School Factor', 'Trasportation Factor']
    	#obj = models.Statistic.objects.get(pk = self.kwargs.get('pk'))
    	print(self.kwargs.get('pk'))
    	defaultData = [1,2,3,4,5]
    	#defaultData = [obj.o1, obj.o2, obj.o3, obj.o4, obj.o5]
    	data = { 'labels' : labels,
    			'defaultData' : defaultData,
    			# 'sales':100,
    			# 'customers':10,
    			# 'users': User.objects.all().count(),
    			}
    	return Response(data)
    	