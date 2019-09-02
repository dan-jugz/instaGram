from django.shortcuts import render,redirect
from .models import Image, Follow
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_intro(request):
    return render(request, 'intro/signin.html')

@login_required(login_url='/accounts/login/')
def index(request):
    title = 'Instagram'
    images = Image.objects.all()
    images_total = images.count()
    print('='*10, images_total)
    for i in images:
        print('^'* 30)
        print(i.uploaded_by)
    print(images)
    all_users = User.objects.all()
    
    return render(request, 'suggestions/suggestions.html', {'title':title, 'images':images, 'all_users':all_users, 'current_user_id':request.user.id})
