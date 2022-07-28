from django.urls import path
from .views import IndividualProfileViewSet, ExperienceDetailViewSet, EducationDetailViewSet, TrainingDetailViewSet, \
    ProjectDetailViewSet, SearchListView, SeekerSkillSetViewSet, SkillSetViewSet, SocialNetworkViewSet, \
    RecommendJobs, Resume
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile', IndividualProfileViewSet, basename='seeker_profile')
router.register('experience', ExperienceDetailViewSet)
router.register('education', EducationDetailViewSet)
router.register('training', TrainingDetailViewSet)
router.register('project', ProjectDetailViewSet)
router.register('skill', SeekerSkillSetViewSet)
router.register('add_skill', SkillSetViewSet)
router.register('social_network', SocialNetworkViewSet)

urlpatterns = [
                  path('search/', SearchListView.as_view(), name='search'),
                  path('resume/', Resume.as_view(), name='resume'),
                  path('recommend/', RecommendJobs.as_view(), name='recommend'),

              ] + router.urls
