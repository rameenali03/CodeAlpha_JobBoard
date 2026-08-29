from django.db import models
from django.contrib.auth.models import User

class CandidateProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="candidate_profile"
    )
    full_name = models.CharField(max_length=150)

    def __str__(self):
        return self.full_name


class EmployerProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="employer_profile"
    )
    company_name = models.CharField(max_length=150)

    def __str__(self):
        return self.company_name    
