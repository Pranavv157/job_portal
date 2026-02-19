from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .decorators import candidate_required, recruiter_required
from .models import Job, Application
from .forms import JobForm, ApplicationForm
from .services import filter_jobs
from .utils import paginate_queryset



# Public job list (landing page)
def job_list(request):
    jobs = Job.objects.filter(is_active=True)
    page_obj = paginate_queryset(request, jobs)
    return render(request, "jobs/job_list.html", {"page_obj": page_obj})


# Recruiter creates a job

@login_required
@recruiter_required
def create_job(request):

    form = JobForm(request.POST or None)

    if form.is_valid():
        job = form.save(commit=False)
        job.recruiter = request.user
        job.save()
        return redirect("recruiter_home")

    return render(request, "jobs/create_job.html", {"form": form})


# Candidate applies to a job
@login_required
@candidate_required
def apply_job(request, job_id):

    job = get_object_or_404(Job, id=job_id)

    # Prevent duplicate applications
    if Application.objects.filter(job=job, candidate=request.user).exists():
        return redirect("candidate_home")

    form = ApplicationForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        application = form.save(commit=False)
        application.job = job
        application.candidate = request.user
        application.save()
        return redirect("candidate_home")

    return render(request, "jobs/apply_jobs.html", {
        "form": form,
        "job": job
    })
# Recruiter views applicants
@login_required
@recruiter_required
def my_applicants(request):

    jobs = Job.objects.filter(recruiter=request.user)
    applications = Application.objects.filter(job__in=jobs)

    return render(request, "jobs/applicant.html", {
        "applications": applications
    })

# Recruiter dashboard
@login_required
@recruiter_required
def recruiter_home(request):

    query = request.GET.get("search", "")
    location = request.GET.get("location", "")

    jobs = Job.objects.filter(recruiter=request.user)
    jobs = filter_jobs(jobs, query, location)

    all_locations = Job.objects.filter(recruiter=request.user)\
                               .values_list("location", flat=True)\
                               .distinct()

    page_obj = paginate_queryset(request, jobs)

    return render(request, "jobs/recruiter_home.html", {
        "page_obj": page_obj,
        "search_query": query,
        "selected_location": location,
        "locations": all_locations
    })

# Candidate dashboard
@login_required
@candidate_required
def candidate_home(request):

    query = request.GET.get("search", "")
    location = request.GET.get("location", "")

    jobs = Job.objects.filter(is_active=True)
    jobs = filter_jobs(jobs, query, location)

    all_locations = Job.objects.filter(is_active=True)\
                               .values_list("location", flat=True)\
                               .distinct()

    page_obj = paginate_queryset(request, jobs)

    return render(request, "jobs/candidate_home.html", {
        "page_obj": page_obj,
        "search_query": query,
        "selected_location": location,
        "locations": all_locations
    })
# Candidate applications page
@login_required
def my_applications(request):

    applications = Application.objects.filter(candidate=request.user)

    return render(request, "jobs/my_applications.html", {
        "applications": applications
    })
