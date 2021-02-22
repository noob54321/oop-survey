from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app.exam.urls')),
    path('admin/', admin.site.urls),
]
