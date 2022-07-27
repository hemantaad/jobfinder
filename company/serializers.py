from rest_framework import serializers
from .models import CompanyProfile, JobPost, JobType, JobPostActivity, CompanyRatings
from user.serializers import AddressSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer


class CompanyProfileSerializer(WritableNestedModelSerializer):
    address = AddressSerializer(required=True)

    class Meta:
        model = CompanyProfile
        fields = '__all__'


class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = '__all__'


class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = '__all__'


class JobPostActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPostActivity
        fields = '__all__'


class CompanyRatingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CompanyRatings
        fields = '__all__'
