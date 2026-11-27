from django.db import models




#user model=userreg
class userreg(models.Model):
    name = models.CharField(max_length=25, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    address = models.TextField(max_length=250, null=True, blank=True)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)

    email = models.EmailField(unique=True, null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    Phone = models.IntegerField(null=True, blank=True)  # FIXED
    Image = models.FileField(upload_to='userphoto/', null=True, blank=True)





#helpline model=helpreg
class HelplineRegister(models.Model):
    office_name = models.CharField(max_length=200)
    helpline_type = models.CharField(max_length=200)
    officer_name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=10)
    address = models.TextField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=20)
    profile_photo = models.ImageField(upload_to='profile/')
    id_proof = models.ImageField(upload_to='idproof/')
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    isapproved = models.BooleanField(default=True)  


# societyreg model=societyreg

from django.db import models

class SocialMediaUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    bio = models.TextField(max_length=300, blank=True, null=True)
    password = models.CharField(max_length=255)
    image = models.ImageField(upload_to="socialProfile/", null=True, blank=True)

    address = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name




#case registration

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

def generate_case_number():
    last_case = MissingChildCase.objects.order_by('-id').first()
    if not last_case:
        return "CMR0001"
    last_num = int(last_case.case_number.replace("CMR", ""))
    new_num = last_num + 1
    return f"CMR{new_num:04d}"


class MissingChildCase(models.Model):
    user = models.ForeignKey('childmissedapp.userreg', on_delete=models.CASCADE)

    helpline = models.ForeignKey(
        'childmissedapp.HelplineRegister',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('FOUND', 'Found'),
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    case_number = models.CharField(max_length=10, unique=True, blank=True)
    child_name = models.CharField(max_length=200)
    child_age = models.IntegerField()
    gender = models.CharField(max_length=20)
    identification_marks = models.TextField()
    description = models.TextField()
    missing_location = models.CharField(max_length=300)
    missing_date = models.DateField()
    missing_time = models.TimeField(default='12:00')
    photo = models.ImageField(upload_to='child_photos/', null=True, blank=True)
    video = models.FileField(upload_to='child_videos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        if not self.case_number:
            self.case_number = generate_case_number()
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.child_name} ({self.case_number})"


    
   


#helpline case aploud
from django.db import models

class MissingChildImage(models.Model):
    photo = models.ImageField(upload_to='child_photos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    matched_child = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"Child Image {self.id}"


#lattitude and longitude
class Marker(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    lat = models.FloatField()
    lng = models.FloatField()

    def _str_(self):
        return self.title  
    





    #societyalert 

class SocietyAlert(models.Model):
    case = models.ForeignKey(MissingChildCase, on_delete=models.CASCADE)
    society_user = models.ForeignKey(SocialMediaUser, on_delete=models.CASCADE)

    alert_message = models.TextField()
    alert_lat = models.FloatField()
    alert_lng = models.FloatField()

    # society report fields
    found_lat = models.FloatField(null=True, blank=True)
    found_lng = models.FloatField(null=True, blank=True)
    found_photo = models.ImageField(upload_to='found_photos/', null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=[('SENT', 'Sent'), ('REPORTED', 'Reported')],
        default='SENT'
    )

    created_at = models.DateTimeField(auto_now_add=True)

