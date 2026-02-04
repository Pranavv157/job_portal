from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required


def register_view(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("dashboard")

    return render(request, "accounts/register.html", {"form": form})


@login_required
def dashboard(request):
    return render(request, "dashboard.html")
