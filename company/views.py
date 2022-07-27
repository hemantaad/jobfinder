from rest_framework import viewsets
from .models import CompanyProfile, JobPost, JobType, JobPostActivity, CompanyRatings
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import CompanyProfileSerializer, JobPostSerializer, JobTypeSerializer, JobPostActivitySerializer, \
    CompanyRatingSerializer
from .filter_sets import JobPostFilter
from rest_framework.permissions import IsAuthenticated
from .permissions import CompanyEditPermission, IsOwner, JobPostPermission, IsStaff
from seeker.permissions import IsSeeker
from django_filters import rest_framework as filters


class CompanyProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner, CompanyEditPermission]
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer


class JobTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsStaff]
    queryset = JobType.objects.all()
    serializer_class = JobTypeSerializer


class CompanyRatingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSeeker]
    queryset = CompanyRatings.objects.all()
    serializer_class = CompanyRatingSerializer


class JobPostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner, JobPostPermission]
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = JobPostFilter


class JobPostActivityViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = JobPostActivity.objects.all()
    serializer_class = JobPostActivitySerializer


# Search Filter
class JobPostListView(generics.ListAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    filter_backends = [SearchFilter, OrderingFilter, filters.DjangoFilterBackend]
    search_fields = ['job_type__job_type', 'job_description']
