from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Job
from .forms import JobForm
from .models import Application
from .forms import ApplicationForm
from django.shortcuts import get_object_or_404



def job_list(request):
    jobs = Job.objects.filter(is_active=True)
    return render(request, "jobs/job_list.html", {"jobs": jobs})


@login_required
def create_job(request):
    # only recruiter allowed
    if request.user.role != "recruiter":
        return redirect("job_list")

    form = JobForm(request.POST or None)

    if form.is_valid():
        job = form.save(commit=False)
        job.recruiter = request.user
        job.save()
        return redirect("job_list")

    return render(request, "jobs/create_job.html", {"form": form})

@login_required
def apply_job(request, job_id):

    if request.user.role != "candidate":
        return redirect("job_list")

    job = get_object_or_404(Job, id=job_id)

    form = ApplicationForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        app = form.save(commit=False)
        app.job = job
        app.candidate = request.user
        app.save()
        return redirect("job_list")

    return render(request, "jobs/apply_job.html", {"form": form, "job": job})

@login_required
def my_applicants(request):
    jobs = Job.objects.filter(recruiter=request.user)
    applications = Application.objects.filter(job__in=jobs)

    return render(request, "jobs/applicants.html", {"applications": applications})




