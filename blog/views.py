from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    hoten ="duy minh"
    lop = "8"
    diem = [10,9,0] #toan ly hoa
    return render(request,'blog/home.html',{
        'username':hoten,
        'class':lop,
        'grade':diem,
    


        })
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        return render(request, 'blog/register.html',{
            'username': username,
            'password': password
    
        })
    return render(request, 'blog/register.html')



# Create your views here.
