from rest_framework import viewsets
from .models import CompanyProfile, CompanyRatings
from .serializers import CompanyProfileSerializer, CompanyRatingSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import CompanyEditPermission, IsOwner
from individual.permissions import IsIndividual


class CompanyProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner, CompanyEditPermission]
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer


class CompanyRatingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsIndividual]
    queryset = CompanyRatings.objects.all()
    serializer_class = CompanyRatingSerializer
