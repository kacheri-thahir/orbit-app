from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

# Create profile automatically when new user is created 


'''sender: the model class that sent the signal (here it will always be User).

instance: the actual object being saved (in this case, the user that was just created).

created: a boolean. It's True only if the user was created for the first time (not updated).

**kwargs: extra data Django may pass.

Inside:

if created: → Only run the code when a new user is created, not when updating.

Profile.objects.create(user=instance) → Makes a new Profile and links it to that User.'''



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Save profile automatically when user is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()