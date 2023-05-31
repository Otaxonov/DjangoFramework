from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def RegistrationView(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been successfully created. You are now able to Sign In")
            return redirect('blog_home')
        messages.error(request, "Unsuccessful registration. Invalid information.")

    form = UserRegistrationForm()

    context  = {
        'title': 'User Create View',
        'form': form
    }

    return render(request, 'accounts/registration.html', context)

def LoginView(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('blog_home')

        messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()

    context = {
        'title': 'Login',
        'form': form
    }

    return render(request, 'accounts/login.html', context)

def LogoutView(request):

    if request.user.is_authenticated:
        logout(request)
        messages.info(request, "You have successfully logged out.")

    return redirect('blog_home')

@login_required
def AccountEditView(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated successfully!')
            return redirect('accounts_edit')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'title': 'Edit Account',
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'accounts/account.html', context)