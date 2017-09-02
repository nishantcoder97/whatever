from django.shortcuts import render

# Create your views here.
from django.views import View

from home.models import Organisation


class HomePage(View):

    def get(self,request):
        organisations = Organisation.objects.all()
        return render(request, 'home/index.html', {'organisations': organisations})
