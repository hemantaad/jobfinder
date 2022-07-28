from django.db import models
from user.models import User, Address


class IndividualProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    PROFILE_TYPE = (
        ('1', 'Seeker'),
        ('2', 'Provider'),
        ('3', 'Both'),
    )
    profile_type = models.CharField(
        max_length=1,
        choices=PROFILE_TYPE,
    )
    image = models.ImageField(
        upload_to="media/individual", null=True, blank=True, default=None
    )
    date_of_birth = models.DateField()
    primary_contact = models.CharField(max_length=14)
    secondary_contact = models.CharField(max_length=14)
    address = models.ForeignKey(Address, related_name='address', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name


class ExperienceDetail(models.Model):
    seeker_profile = models.ForeignKey(IndividualProfile, related_name='individual', on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    starting_date = models.DateField()
    completion_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.seeker_profile.user.name


class JobLevel(models.Model):
    experience = models.OneToOneField(ExperienceDetail, related_name='job_level', on_delete=models.CASCADE)
    level = models.CharField(max_length=50)

    def __str__(self):
        return self.level


class JobCategory(models.Model):
    experience = models.OneToOneField(ExperienceDetail, related_name='job_category', on_delete=models.CASCADE)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class EducationDetail(models.Model):
    seeker_profile = models.ForeignKey(IndividualProfile, models.CASCADE)
    specialization = models.CharField(max_length=50)
    starting_date = models.DateField()
    completion_date = models.DateField()
    education_board = models.CharField(max_length=50)
    university_name = models.CharField(max_length=50)
    percentage = models.IntegerField()

    def __str__(self):
        return self.seeker_profile.name


class ProjectDetail(models.Model):
    seeker_profile = models.ForeignKey(IndividualProfile, models.CASCADE)
    title = models.CharField(max_length=200)
    starting_date = models.DateField()
    completion_date = models.DateField()
    description = models.TextField()


class TrainingDetail(models.Model):
    seeker_profile = models.ForeignKey(IndividualProfile, models.CASCADE)
    course_name = models.CharField(max_length=50)
    institute_name = models.CharField(max_length=100)
    starting_date = models.DateField()
    completion_date = models.DateField()
    certificate = models.ImageField(
        upload_to="media/certificate", null=True, blank=True, default=None
    )

    def __str__(self):
        return self.course_name


class SkillSet(models.Model):
    skill = models.CharField(max_length=50)

    def __str__(self):
        return self.skill


class SeekerSkillSet(models.Model):
    SKILL_LEVEL = (
        ('1', 'Beginner'),
        ('2', 'Intermediate'),
        ('3', 'Expert'),
    )
    level = models.CharField(
        max_length=1,
        choices=SKILL_LEVEL,
    )
    seeker_profile = models.ForeignKey(IndividualProfile, models.CASCADE)
    skill_set = models.ForeignKey(SkillSet, models.CASCADE)


class SocialNetwork(models.Model):
    seeker_profile = models.ForeignKey(IndividualProfile, models.CASCADE)
    facebook = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)
    github = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)
