from django.db import models
from user.models import User, Address


class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    logo = models.ImageField(
        upload_to="media/owner", null=True, blank=True, default=None
    )
    established_date = models.DateField()
    primary_contact = models.CharField(max_length=14)
    secondary_contact = models.CharField(max_length=14)
    website_url = models.URLField(max_length=200)
    description = models.TextField()
    address = models.ForeignKey(
        Address, related_name='company_address', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name


class CompanyRatings(models.Model):
    RATING_TYPE = (
        ('1', 'Poor'),
        ('2', 'Satisfactory'),
        ('3', 'Good'),
        ('4', 'Excellent'),
    )
    rating_type = models.CharField(
        max_length=1,
        choices=RATING_TYPE,
    )
    review = models.TextField()
    company_profile = models.ForeignKey(
        CompanyProfile, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
