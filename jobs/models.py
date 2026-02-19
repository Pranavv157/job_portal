from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


from django.conf import settings
from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    is_active = models.BooleanField(default=True)  #  IMPORTANT

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    candidate = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job', 'candidate')
