from django.shortcuts import render
from .models import details
# Create your views here.
def employee(request):
    data=details.objects.all()
    return render(request,"one.html",{"context":data})
