from django.urls import path
from .views import job_list, create_job
from .views import apply_job, my_applicants
from .views import recruiter_home, candidate_home,edit_job,delete_job,toggle_job_status
from .views import my_applications
from . import views
urlpatterns = [
    path('', job_list, name='job_list'),
    path('create/', create_job, name='create_job'),
    path('apply/<int:job_id>/', apply_job, name='apply_job'),
    path('applicants/', my_applicants, name='applicants'),
    path('my-applications/', my_applications, name='my_applications'),

    path('recruiter/', recruiter_home, name='recruiter_home'),
    path('candidate/', candidate_home, name='candidate_home'),
    path("job/<int:job_id>/edit/", edit_job, name="edit_job"),
    path("job/<int:job_id>/delete/", delete_job, name="delete_job"),
    path("job/<int:job_id>/toggle/", toggle_job_status, name="toggle_job"),

]
