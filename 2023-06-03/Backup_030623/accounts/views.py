from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from accounts.forms import SignUpForm

# Create your views here.

#def signup(request):
#    #return render(request, 'signup.html')
#    form = UserCreationForm()
#    return render(request, 'signup.html', {'form': form})

def signup(request):
    #print("Signup started")
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        #print(form)
        if form.is_valid():
            #print("Form is valid")
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})




