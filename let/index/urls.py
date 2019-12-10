from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'index'
urlpatterns = [
	
	path('', views.index, name = 'ind'),
	path('test/', views.AddView.as_view(), name = 'ind-add'),
	path('success/<int:pk>/', views.SuccessView.as_view(), name='ind-view'),
	path('api/data/', views.get_data),
	path('api/data/charts/', views.ChartData.as_view()),
	#path('', include('index.urls')),
    #path('admin/', admin.site.urls),
]
