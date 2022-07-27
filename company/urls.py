from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CompanyProfileViewSet, JobPostViewSet, JobTypeViewSet, JobPostActivityViewSet, JobPostListView, \
    CompanyRatingViewSet

router = DefaultRouter()
router.register('profile', CompanyProfileViewSet)
router.register('job-type', JobTypeViewSet)
router.register('job-post', JobPostViewSet)
router.register('job-post-activity', JobPostActivityViewSet)
router.register('rating', CompanyRatingViewSet)

urlpatterns = [
    path('search/', JobPostListView.as_view(), name='search'),
]

urlpatterns += router.urls
