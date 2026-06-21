from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    hoten = "duy minh"
    lop = "8"
    diem = [10, 9, 0] # toan ly hoa
    return render(request, 'blog/home.html', {
        'username': hoten,
        'class': lop,
        'grade': diem,
    })

def register(request):
    username_session = request.session.get('logged_in_user', None)
    

    menu_items = [
{'id': 1, 'name': 'Rộn Ràng 1', 'price': 195000, 'image': 'blog/images/image1111.webp'},
        {'id': 2, 'name': 'Rộn Ràng 2', 'price': 280000, 'image': 'blog/images/image2222.webp'},
        {'id': 3, 'name': 'Yêu Thương 3', 'price': 142000, 'image': 'blog/images/image3333.webp'},
        {'id': 4, 'name': 'Yêu Thương 1', 'price': 142000, 'image': 'blog/images/image4444.webp'},
    ]
    
    discount_code = ""
    is_discounted = False

    if request.method == 'POST':
        discount_code = request.POST.get('discount_code', '').strip()
        if discount_code == "-andawde-":
            is_discounted = True


    for item in menu_items:
        if is_discounted:
            item['display_price'] = f"{item['price']:,} đ"
        else:
            increased_price = int(item['price'] * 1.2)
            item['display_price'] = f"{increased_price:,} đ"

    context = {
        'username': username_session,
        'menu_items': menu_items,
        'discount_code': discount_code,
        'is_discounted': is_discounted
    }
    return render(request, 'blog/register.html', context)

def login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if len(username) < 8 or len(password) < 8 or len(username) > 5000 or len(password) > 5000:
            context['error'] = "your username or password isn't 8 letters or over 5000 letters"
        else:
            request.session['logged_in_user'] = username
            context['username'] = username
            
    return render(request, 'blog/login.html', context)

def lotteria(request):
    return render(request, 'blog/lotteria.html')