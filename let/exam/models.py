from django.db import models


class Personality(models.Model):
	question_1 = models.CharField(max_length = 20)
	question_2 = models.CharField(max_length = 20)
	question_3 = models.CharField(max_length = 20)

	def __str__(self):
		return str(self.question_1)
	
