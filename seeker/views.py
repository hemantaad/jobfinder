from rest_framework import viewsets
from rest_framework.views import APIView

from .models import SeekerProfile, Address, ExperienceDetail, JobCategory, JobLevel, EducationDetail, TrainingDetail, \
    ProjectDetail, SkillSet, SeekerSkillSet, SocialNetwork
from company.models import JobPost
from .serializers import SeekerProfileSerializer, AddressSerializer, ExperienceDetailSerializer, JobCategorySerializer, \
    JobLevelSerializer, EducationDetailSerializer, ProjectDetailSerializer, TrainingDetailSerializer, \
    SkillSetSerializer, SeekerSkillSetSerializer, SocialNetworkSerializer
from company.serializers import JobPostSerializer
from rest_framework import filters, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSeeker, SeekerProfileEditPermission


class SeekerProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSeeker, SeekerProfileEditPermission]
    queryset = SeekerProfile.objects.all()
    serializer_class = SeekerProfileSerializer

    def get_queryset(self):
        queryset = self.get_serializer_class().setup_eager_loading(self.queryset)
        return queryset


class AddressViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSeeker, SeekerProfileEditPermission]
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class JobCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSeeker, SeekerProfileEditPermission]
    queryset = JobCategory.objects.all()
    serializer_class = JobCategorySerializer


class JobLevelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSeeker, SeekerProfileEditPermission]
    queryset = JobLevel.objects.all()
    serializer_class = JobLevelSerializer


class ExperienceDetailViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSeeker, SeekerProfileEditPermission]
    queryset = ExperienceDetail.objects.all()
    serializer_class = ExperienceDetailSerializer

    def get_queryset(self):
        queryset = self.get_serializer_class().setup_eager_loading(self.queryset)
        return queryset


class EducationDetailViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSeeker, SeekerProfileEditPermission]
    queryset = EducationDetail.objects.all()
    serializer_class = EducationDetailSerializer


class ProjectDetailViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSeeker, SeekerProfileEditPermission]
    queryset = ProjectDetail.objects.all()
    serializer_class = ProjectDetailSerializer


class TrainingDetailViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSeeker, SeekerProfileEditPermission]
    queryset = TrainingDetail.objects.all()
    serializer_class = TrainingDetailSerializer


class SkillSetViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSeeker, SeekerProfileEditPermission]
    queryset = SkillSet.objects.all()
    serializer_class = SkillSetSerializer


class SeekerSkillSetViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSeeker, SeekerProfileEditPermission]
    queryset = SeekerSkillSet.objects.all()
    serializer_class = SeekerSkillSetSerializer


class SocialNetworkViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSeeker, SeekerProfileEditPermission]
    queryset = SocialNetwork.objects.all()
    serializer_class = SocialNetworkSerializer


class Resume(APIView):

    def get(self, request, format=None):
        serializer_list = []
        user = self.request.user
        profile = SeekerProfile.objects.filter(user_id=user.id).all()
        experience = ExperienceDetail.objects.filter(seeker_profile__user_id=user.id).all()
        education = EducationDetail.objects.filter(seeker_profile__user_id=user.id).all()
        project = ProjectDetail.objects.filter(seeker_profile__user_id=user.id).all()
        training = TrainingDetail.objects.filter(seeker_profile__user_id=user.id).all()
        profile_serializer = SeekerProfileSerializer(profile, many=True)
        experience_serializer = ExperienceDetailSerializer(experience, many=True)
        education_serializer = EducationDetailSerializer(education, many=True)
        project_serializer = ProjectDetailSerializer(project, many=True)
        training_serializer = TrainingDetailSerializer(training, many=True)
        serializer_list.extend([profile_serializer.data, experience_serializer.data, education_serializer.data,
                                project_serializer.data, training_serializer.data])

        return Response(serializer_list)


# Search Filter
class SearchListView(generics.ListAPIView):
    queryset = TrainingDetail.objects.all()
    serializer_class = TrainingDetailSerializer
    filter_backends = [filters.SearchFilter]
    print(filters.SearchFilter)
    search_fields = ['^course_name']


# Recommend System
class RecommendJobs(APIView):

    def get(self, request, format=None):
        user = self.request.user
        user_course = TrainingDetail.objects.filter(seeker_profile__user__id=user.id).all()
        print(user_course)
        serializer_list = []
        for course in user_course:
            users_course = course.course_name
            recommend_jobs = JobPost.objects.filter(job_type__job_type=users_course).all()
            serializer = JobPostSerializer(recommend_jobs, many=True)
            serializer_list.append(serializer.data)
        return Response(serializer_list)
