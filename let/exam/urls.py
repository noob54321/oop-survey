from django.contrib import admin
from django.urls import path
from . import views

app_name = 'exam'

urlpatterns = [
	path('', views.index, name = 'index'),
	path('let/', views.PersonalityAddView.as_view(), name ='let'),
	path('success/', views.success, name = 'success')
]