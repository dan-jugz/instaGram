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

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            return HttpResponse('<body style="background: #e2e2e2;">Now you can <a href="/accounts/login/">login</a> your account.</body>')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def new_image(request):
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        current_user = request.user
        if form.is_valid():
            image = form.save(commit=False)
            image.uploaded_by = current_user
            image.save()
            print('-' * 30)
            print(image.uploaded_by)
            image.save_image()
            return redirect(index)
    else:
        form = NewImageForm()
    return render(request, 'image/new_image.html', {'form':form})
