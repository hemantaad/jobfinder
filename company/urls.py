from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CompanyProfileViewSet, CompanyRatingViewSet

router = DefaultRouter()
router.register('profile', CompanyProfileViewSet)
router.register('rating', CompanyRatingViewSet)

urlpatterns = [

]

urlpatterns += router.urls
