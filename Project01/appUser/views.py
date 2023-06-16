from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from .forms import AuthenticationForm


def get_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("get_all_topic")
        return render(request, "registration.html", context={'form': form})
    form = UserCreationForm(request.POST)
    return render(request, "registration.html", context={'form': form})


def my_login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AuthenticationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # some actions
            login(request, form.user)
            return redirect("get_all_topic")
        return render(request, "login.html", {'form': form})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {'form': form})


def logout_view(request):
    logout(request)
    return redirect("my_login")
