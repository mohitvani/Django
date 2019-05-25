from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm , UserUpdatForm , profileUpdatForm
from django.contrib.auth.decorators import login_required

#  pip install pillow

# Create your views here.

# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request , f'Account ctreated for{username}!')
#             return redirect('blog-home')

#     else:

#         form = UserCreationForm
#     return render(request , "users/register.html" , {"form" : form})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request , f'Your Account has been created! You can now login')
            return redirect('login')

    else:

        form = UserRegistrationForm()
    return render(request , "users/register.html" , {"form" : form})

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdatForm(request.POST , instance = request.user)
        p_form = profileUpdatForm(request.POST , request.FILES,instance= request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request , f'Your Account has been updated!')
            return redirect('profile')

    u_form = UserUpdatForm(instance = request.user)
    p_form = profileUpdatForm(instance= request.user.profile)
    

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request , "users/profile.html" , context)
 