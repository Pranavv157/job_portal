from django.shortcuts import redirect
from functools import wraps

def recruiter_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.role != "recruiter":
            return redirect("candidate_home")
        return view_func(request, *args, **kwargs)
    return wrapper


def candidate_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.role != "candidate":
            return redirect("recruiter_home")
        return view_func(request, *args, **kwargs)
    return wrapper
