from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate


from .forms import CustomUserCreationForm
from .models import CustomUser



def signUp(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data('username')
            raw_password = form.cleaned_data('password1')
            age = form.cleaned_data('age')
            city = form.cleaned_data('city')
            
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})

