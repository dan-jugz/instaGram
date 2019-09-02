from django.shortcuts import render, redirect
from homepage.models import Image, Follow
from django.contrib.auth.decorators import login_required
from .forms import NewProfileForm, NewImageForm
from homepage.models import Profile

# Create your views here.

@login_required(login_url='/accounts/login')
def profile_page(request):
    current_user = request.user
    print('-'* 40)
    print(current_user.id)
    all_images = Image.objects.all()
    all_instagram_followers = Follow.objects.all()
    following = Follow.objects.filter(user_id=current_user.id)
    print('=>'*10, following.count())
    user_images = []
    for j in all_images:
        if j.uploaded_by==current_user:
            print(j.uploaded_by)
            user_images.append(j.image)
    print('+' * 30)
    print(user_images)
    return render(request, 'profile/profile_page.html', {'user_images':user_images, 'following':following.count()})

@login_required(login_url='/accounts/login')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST'  :
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        print('*' * 30)
        print(bio)
        print('*' * 30)
        print(first_name, last_name, phone, email)
        user_id = current_user.id
        if Profile.objects.filter(user_id=user_id):
            user = Profile.objects.filter(user_id=user_id)
           
            form = NewProfileForm(request.POST, request.FILES)
            if form.is_valid():
                form = form.save()
        
            print('*' * 30)
            # print(user)
            user.update(first_name=first_name, last_name=last_name,phone=phone, email=email, bio=bio)
        else: 
            new_profile = Profile.objects.create(user_id=current_user.id, first_name=first_name, last_name=last_name,email=email,phone=phone, bio=bio)
    return redirect(edit_profile_page)
        