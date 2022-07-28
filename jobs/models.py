from django.db import models
from individual.models import IndividualProfile
from user.models import User


class JobType(models.Model):
    job_type = models.CharField(max_length=150)

    def __str__(self):
        return self.job_type


class JobPost(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    job_type = models.ManyToManyField(JobType)
    created_date = models.DateField()
    job_description = models.TextField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.posted_by.name


class JobPostActivity(models.Model):
    seeker_profile = models.ForeignKey(
        IndividualProfile, on_delete=models.CASCADE)
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    apply_date = models.DateField(auto_now_add=True)
