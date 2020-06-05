from django.shortcuts import render, redirect
from register.forms import RegisterForm


# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/registration_success")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form})


def registration_success(request):
    return render(request, "register/registration_success.html")
