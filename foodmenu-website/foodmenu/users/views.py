from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.


def user_register(request):
    print('hey')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, you accout was created')
            return redirect('food:index')
        else:
            return render(request, 'users/register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'users/register.html', {'form': form})
