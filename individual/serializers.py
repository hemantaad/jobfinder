from rest_framework import serializers
from .models import IndividualProfile, JobLevel, JobCategory, ExperienceDetail, EducationDetail, ProjectDetail, \
    TrainingDetail, SkillSet, SeekerSkillSet, SocialNetwork
from drf_writable_nested.serializers import WritableNestedModelSerializer
from user.serializers import AddressSerializer


class IndividualProfileSerializer(WritableNestedModelSerializer):
    address = AddressSerializer(required=True)

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related('user').prefetch_related('address')
        # queryset = queryset.select_related('user')
        # queryset = queryset.all()
        return queryset

    class Meta:
        model = IndividualProfile
        fields = [
            'id',
            'date_of_birth',
            'primary_contact',
            'secondary_contact',
            'user',
            'profile_type',
            'address'
        ]


class JobLevelSerializer(WritableNestedModelSerializer):
    class Meta:
        model = JobLevel
        fields = [
            'level',
        ]


class JobCategorySerializer(WritableNestedModelSerializer):
    class Meta:
        model = JobCategory
        fields = [
            'category'
        ]


class ExperienceDetailSerializer(WritableNestedModelSerializer):

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.prefetch_related('seeker_profile__user').select_related('job_level', 'job_category')
        return queryset

    # Reverse OneToOne relation
    job_level = JobLevelSerializer(required=True)
    job_category = JobCategorySerializer(required=True)

    class Meta:
        model = ExperienceDetail
        fields = [
            "seeker_profile",
            "organization_name",
            "designation",
            "starting_date",
            "completion_date",
            "description",
            "job_level",
            "job_category",
        ]


class EducationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationDetail
        fields = '__all__'


class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDetail
        fields = '__all__'


class TrainingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingDetail
        fields = '__all__'


class SkillSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillSet
        fields = '__all__'


class SeekerSkillSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeekerSkillSet
        fields = '__all__'


class SocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = '__all__'


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualProfile, ExperienceDetail
        fields = [
            'date_of_birth',
            'primary_contact',
            'secondary_contact',
            'organization_name',
        ]
