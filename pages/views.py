from django.shortcuts import render


from django.http import HttpResponse

def about(request):
    return render(request,'pages/about.html')

# Create your views here.
