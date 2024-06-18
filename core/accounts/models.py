from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserManager(BaseUserManager):
    """
    Custom manager for User model with no username field.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular user with the given email and password.
        """
        if not email:  # Check if email is provided
            raise ValueError("The email must be set.")
        
        email = self.normalize_email(email)  # Normalize email
        user = self.model(email=email, **extra_fields)  # Create user instance
        user.set_password(password)  # Set user password
        user.save()  # Save user to database
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)  # Ensure is_staff is True
        extra_fields.setdefault('is_superuser', True)  # Ensure is_superuser is True
        extra_fields.setdefault('is_active', True)  # Ensure is_active is True
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        
        return self.create_user(email, password, **extra_fields)  # Create superuser


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model that replaces username with email.
    """
    email = models.EmailField(max_length=255, unique=True)  # Email field
    is_superuser = models.BooleanField(default=False)  # Superuser flag
    is_staff = models.BooleanField(default=False)  # Staff flag
    is_active = models.BooleanField(default=True)  # Active flag
    date_joined = models.DateTimeField(auto_now_add=True)  # Date joined
    
    created_at = models.DateTimeField(auto_now_add=True)  # Created at timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Updated at timestamp
    
    USERNAME_FIELD = 'email'  # Use email for login
    REQUIRED_FIELDS = []  # No additional required fields
    
    objects = UserManager()  # Manager for user model


class Profile(models.Model):
    """
    Profile model linked to User.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User foreign key
    first_name = models.CharField(max_length=250)  # First name
    last_name = models.CharField(max_length=250)  # Last name
    image = models.ImageField(blank=True, null=True)  # Profile image
    description = models.TextField()  # Description
    created_at = models.DateTimeField(auto_now_add=True)  # Created at timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Updated at timestamp
    
    def __str__(self):
        return self.user.email  # String representation


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    """
    Signal to create Profile when a new User is created.
    """
    if created:  # Check if the user is created
        Profile.objects.create(user=instance)  # Create profile for user
