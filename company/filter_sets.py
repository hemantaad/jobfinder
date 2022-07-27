from rest_framework import generics
from django_filters import rest_framework as filters
from .models import JobPost


class JobPostFilter(filters.FilterSet):
    class Meta:
        model = JobPost
        fields = {
            "posted_by__user__name": ["exact"],
            "job_type__job_type": ["exact"],
            "created_date": ["exact"],
        }
