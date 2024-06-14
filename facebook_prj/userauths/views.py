from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from userauths.models import Profile, User
from django.http import HttpResponseRedirect


from core.models import Post, FriendRequest


# Create your views here.


def RegisterView(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are registered!")
        return redirect("core:feed")
    

    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save()

        full_name = form.cleaned_data.get("full_name")
        phone = form.cleaned_data.get("phone")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")

        user = authenticate(email = email, password = password)

        if user:
            login(request, user)

            profile = Profile.objects.get(user = request.user)
            profile.full_name = full_name
            profile.phone = phone
            profile.save()

            messages.success(request, f"Hi, {full_name}, your account was created successfully")
            return redirect("core:feed")
        else:
            messages.error(request, "Authentication failed. Please try again.")
    else:
        print(form.errors)
        messages.error(request, "There was an error with your form. Please check your input.")
    

    context = {
        "form" : form
    }

    return render(request, "userauths/sign-up.html", context)







def LoginView(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already login!")
        return redirect("core:feed")
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email = email)
            user = authenticate(request, email = email, password = password)
            if user is not None:
                login(request,user)
                messages.success(request, "You are logged in")
                return redirect("core:feed")
            
            else:
                messages.error(request, "Username or password does not match")
                return redirect("userauths:sign-up")

        except:
            messages.error(request, "User does not exist")
            return redirect("userauths:sign-up")

    return HttpResponseRedirect("/")





def LogoutView(request):
    logout(request)
    messages.success(request, "You are looged out!")
    return redirect("userauths:sign-up")



@login_required
def my_profile(request):
    profile = request.user.profile
    posts = Post.objects.filter(active = True, user = request.user)

    context = {
        "profile" : profile,
        "posts": posts,
    }

    return render(request, "userauths/my-profile.html", context)




@login_required
def friend_profile(request, username):
    profile = Profile.objects.get(user__username = username)
    posts = Post.objects.filter(active = True, user = profile.user)

    bool = False
    bool_friend = False

    sender = request.user
    receiver = profile.user

    try:
        friend_request = FriendRequest.objects.get(sender = sender , receiver = receiver)
        if friend_request:
            bool = True

        else:
            bool = False

    except:
        bool = False



    context = {
        "profile": profile,
        "posts": posts,
        "bool": bool,
    }


    return render(request, "userauths/friend-profile.html", context)













