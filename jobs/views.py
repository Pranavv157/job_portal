from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Job, Application
from .forms import JobForm, ApplicationForm
from django.core.paginator import Paginator


# Public jobs list
def job_list(request):
    jobs = Job.objects.filter(is_active=True)
    return render(request, "jobs/job_list.html", {"jobs": jobs})


# Recruiter creates job
@login_required
def create_job(request):

    if request.user.role != "recruiter":
        return redirect("candidate_home")   

    form = JobForm(request.POST or None)

    if form.is_valid():
        job = form.save(commit=False)
        job.recruiter = request.user
        job.save()
        return redirect("recruiter_home")  

    return render(request, "jobs/create_job.html", {"form": form})



# Candidate applies
@login_required
def apply_job(request, job_id):

    if request.user.role != "candidate":
        return redirect("recruiter_home")   

    job = get_object_or_404(Job, id=job_id)

    form = ApplicationForm(request.POST or None, request.FILES or None)

    if Application.objects.filter(job=job, candidate=request.user).exists():
        return redirect("candidate_home")

    if form.is_valid():
        app = form.save(commit=False)
        app.job = job
        app.candidate = request.user
        app.save()
        return redirect("candidate_home")

    return render(request, "jobs/apply_jobs.html", {"form": form, "job": job})



# Recruiter views applicants
@login_required
def my_applicants(request):

    if request.user.role != "recruiter":
        return redirect("candidate_home")   

    jobs = Job.objects.filter(recruiter=request.user)
    applications = Application.objects.filter(job__in=jobs)

    return render(request, "jobs/applicant.html", {"applications": applications})



# Recruiter dashboard
@login_required
def recruiter_home(request):

    if request.user.role != "recruiter":
        return redirect("candidate_home")

    query = request.GET.get("search","")

    jobs = Job.objects.filter(recruiter=request.user)

    if query:
        jobs = jobs.filter(
            title__icontains=query
        ) | jobs.filter(
            company__icontains=query
        )
    paginator = Paginator(jobs, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "jobs/recruiter_home.html", {
        "page_obj": page_obj,
        "search_query": query
    })


# Candidate dashboard
@login_required
def candidate_home(request):

    if request.user.role != "candidate":
        return redirect("recruiter_home")

    query = request.GET.get("search","")

    jobs = Job.objects.filter(is_active=True)

    if query:
        jobs = jobs.filter(
            title__icontains=query
        ) | jobs.filter(
            company__icontains=query
        )
    paginator = Paginator(jobs, 5)  # 5 jobs per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "jobs/candidate_home.html", {
        "page_obj": page_obj,
        "search_query": query
    })

@login_required
def my_applications(request):

    if request.user.role != "candidate":
        return redirect("recruiter_home")

    applications = Application.objects.filter(candidate=request.user)

    return render(request, "jobs/my_applications.html", {
        "applications": applications
    })
