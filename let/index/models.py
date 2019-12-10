from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

# Create your models here.
alpha = RegexValidator(regex=r'^[a-zA-Z ]*$', message='Only Alphabets are allowed',)

class Statistic(models.Model) :

	name  = models.CharField(max_length = 100)
	course = models.CharField(max_length = 100)
	university = models.CharField(max_length = 100)

	#Personal
	f1 = models.IntegerField(verbose_name = 'Personal Factor 1')
	f2 = models.IntegerField(verbose_name = 'Personal Factor 2')
	f3 = models.IntegerField(verbose_name = 'Personal Factor 3')
	f4 = models.IntegerField(verbose_name = 'Personal Factor 4')
	f5 = models.IntegerField(verbose_name = 'Personal Factor 5')

	#Family
	f6 = models.IntegerField(verbose_name = 'Family Factor 1')
	f7 = models.IntegerField(verbose_name = 'Family Factor 2')
	f8 = models.IntegerField(verbose_name = 'Family Factor 3')
	f9 = models.IntegerField(verbose_name = 'Family Factor 4')
	f10 = models.IntegerField(verbose_name = 'Family Factor 5')

	#Peer
	f11 = models.IntegerField(verbose_name = 'Peer Factor 1')
	f12 = models.IntegerField(verbose_name = 'Peer Factor 2')
	f13 = models.IntegerField(verbose_name = 'Peer Factor 3')
	f14 = models.IntegerField(verbose_name = 'Peer Factor 4')
	f15 = models.IntegerField(verbose_name = 'Peer Factor 5')

	#School
	f16 = models.IntegerField(verbose_name = 'School Factor 1')
	f17 = models.IntegerField(verbose_name = 'School Factor 2')
	f18 = models.IntegerField(verbose_name = 'School Factor 3')
	f19 = models.IntegerField(verbose_name = 'School Factor 4')
	f20 = models.IntegerField(verbose_name = 'School Factor 5')	

	#Other na di ko alam
	f21 = models.IntegerField(verbose_name = 'Miscellenaous Factor 1')
	f22 = models.IntegerField(verbose_name = 'Miscellenaous Factor 2')
	f23 = models.IntegerField(verbose_name = 'Miscellenaous Factor 3')
	f24 = models.IntegerField(verbose_name = 'Miscellenaous Factor 4')
	f25 = models.IntegerField(verbose_name = 'Miscellenaous Factor 5')	

	total = models.IntegerField(default = 0 , null=True, verbose_name = 'Total')
	over = models.DecimalField(decimal_places=2, max_digits=12, default=0, null=True, verbose_name='Average')

	o1 = models.IntegerField(default=0, null=True, verbose_name='Overall 1') 	
	o2 = models.IntegerField(default=0, null=True, verbose_name='Overall 2')
	o3 = models.IntegerField(default=0, null=True, verbose_name='Overall 3')
	o4 = models.IntegerField(default=0, null=True, verbose_name='Overall 4')
	o5 = models.IntegerField(default=0, null=True, verbose_name='Overall 5')

	def __str__(self):
		return self.name

	@staticmethod
	def Max():
		return 125

	@staticmethod
	def Each():
		return 25

	def Percentage(self):
		return self.over * 100

	def O1(self):
		return self.o1 / self.Each()

	def O2(self):
		return self.o2 / self.Each()

	def O3(self):
		return self.o3 / self.Each()

	def O4(self):
		return self.o4 / self.Each()

	def O5(self):
		return self.o5 / self.Each()

	def TotalO(self):
		return self.O1() + self.O2() + self.O3() + self.O4() + self.O5()

	def Calls(self):
		if 25 <= self.total < 49:
			return "Low Chance"
		if 50 <= self.total < 74:
			return "Average Chance"
		if 75 <= self.total < 99 :
			return "High Chance"
		return "Very High Chance"
