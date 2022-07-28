from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import JobPostViewSet, JobTypeViewSet, JobPostActivityViewSet, JobPostListView

router = DefaultRouter()
router.register('type', JobTypeViewSet)
router.register('post', JobPostViewSet)
router.register('activity', JobPostActivityViewSet)

urlpatterns = [
    path('search/', JobPostListView.as_view(), name='search'),
]

urlpatterns += router.urls