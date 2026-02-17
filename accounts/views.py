from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm


from django.http import HttpResponse
from django.contrib.auth import get_user_model

User = get_user_model()

def fix_roles(request):
    updated = User.objects.filter(role__isnull=True).update(role="candidate")
    return HttpResponse(f"Fixed {updated} users")

#  Central role-based redirect 
@login_required
def post_login_redirect(request):
    if request.user.role == "candidate":
        return redirect("candidate_home")
    elif request.user.role == "recruiter":
        return redirect("recruiter_home")
    return redirect("/")


#  Register view with next support
def register_view(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        login(request, user)

        # IMPORTANT: preserve next
        next_url = request.POST.get("next") or request.GET.get("next")
        return redirect(next_url or "post_login_redirect")

    return render(request, "accounts/register.html", {
        "form": form
    })


#  Optional dashboard (safe fallback)
@login_required
def dashboard(request):
    return redirect("post_login_redirect")


#  Logout → landing page
@login_required
def logout_view(request):
    logout(request)
    return redirect("/")
