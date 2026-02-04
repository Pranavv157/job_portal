from django.urls import path
from .views import job_list, create_job
from .views import apply_job, my_applicants
urlpatterns = [
    path('', job_list, name='job_list'),
    path('create/', create_job, name='create_job'),
    path('apply/<int:job_id>/', apply_job, name='apply_job'),
    path('applicants/', my_applicants, name='applicants'),

]
