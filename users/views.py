from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from users.models import User,UserForm,LoginForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})  

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'user_detail.html', {'user': user})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})

def user_update(request, pk):
    user= get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'user_form.html', {'form': form})

def user_delete(request, pk):
    user= get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        User.delete()
        return redirect('user_list')
    return render(request, 'user_confirm_delete.html', {'user': user})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                form.add_error('email', 'User with this email does not exist.')
                return render(request, 'user_login_form.html', {'form': form})
    else:
        form = LoginForm()
    
    return render(request, 'user_login_form.html', {'form': form})



def login_view(request):
    if request.method == "POST":
        email= request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.get(email=email)

        if user is not None:
            ##login(request, user)
            messages.success(request, f"Welcome back, {user.email}!")
            return redirect("member_list")  # change to your homepage URL name
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "login.html")


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("login")