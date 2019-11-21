from django.shortcuts import render
from django.views import View

# Create your views here.
class LandingView(View):
    template_name = 'landing.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, 'srvy/landing.html', {})
