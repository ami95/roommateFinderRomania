from django.db import models
from django.contrib.auth.models import User
from datetime import date

from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    '''We will be Extending The User Model Using a One-To-One Link'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    dob = models.DateField(default=datetime.date(1989, 12, 25))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    city = models.CharField(max_length=100)
    description = models.TextField()
    ocupation = models.CharField(max_length=100)
    monthly_budget = models.IntegerField()
    tidyness_lvl = models.IntegerField()

    is_smoker = models.BooleanField(default = False)
    has_pets = models.BooleanField(default = False)

    image = models.ImageField(upload_to='media')

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering = ['user']

    def __str__(self):
        return self.user.username

    def age(dob):
        today = date.today()
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))


'''
Now this is where the magic happens: we will now define signals so our Profile model
will be automatically created/updated when we create/update User instances.
For this we must import 'post_save' & 'receiver'

Basically we are hooking the create_user_profile and save_user_profile methods
to the User model, whenever a save event occurs.
This kind of signal is called post_save.
'''

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
