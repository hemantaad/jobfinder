from django.contrib import admin
from .models import JobType, JobPost, JobPostActivity
admin.site.register(JobType)
admin.site.register(JobPost)
admin.site.register(JobPostActivity)

