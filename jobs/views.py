from rest_framework import viewsets
from .models import JobPost, JobType, JobPostActivity
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import JobPostSerializer, JobTypeSerializer, JobPostActivitySerializer
from .filter_sets import JobPostFilter
from rest_framework.permissions import IsAuthenticated
from company.permissions import IsOwner
from individual.permissions import IsIndividual, IsIndividualProvider
from .permissions import JobPostPermission
from django_filters import rest_framework as filters


class JobTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = JobType.objects.all()
    serializer_class = JobTypeSerializer


class JobPostViewSet(viewsets.ModelViewSet):
    permission_classes = [
        IsAuthenticated,
        IsIndividualProvider |
        IsOwner,
    ]
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = JobPostFilter


class JobPostActivityViewSet(viewsets.ModelViewSet):
    permission_classes = [
        IsAuthenticated,
        IsOwner |
        IsIndividualProvider,
    ]
    queryset = JobPostActivity.objects.all()
    serializer_class = JobPostActivitySerializer


# Search Filter
class JobPostListView(generics.ListAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    filter_backends = [SearchFilter,
                       OrderingFilter, filters.DjangoFilterBackend]
    search_fields = [
        'job_type__job_type',
        'job_description',
        'posted_by__name'
    ]
