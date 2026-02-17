from django.db.models import Q

def filter_jobs(jobs, query="", locations=""):
    if query:
        jobs = jobs.filter(
            Q(title__icontains=query) |
            Q(company__icontains=query)
        )

    if locations:
        jobs = jobs.filter(location__icontains=locations)

    return jobs
