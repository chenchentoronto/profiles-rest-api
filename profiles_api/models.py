from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManger(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None): # if not set the password, it would default by None
        """Create a new user profile"""
        if not email:
            """if the email is an empty string or a null value, we will raise exception"""
            raise ValueError("User must have an email address")
        email = self.normalize_email(email)

        # This won't call/run the class definition again
        # Called UserProfile.objects.create_user("a@example.com", "Alice", "password123")
        # and then Django will run the UserProfile.__init__() to create a instance
        user = self.model(email=email, name=name) # Create a new UserProfile. here self.model = self.UserProfile(email, name)
        user.set_password(password) # password is encrypted
        user.save(using=self._db) # save data it to the database
        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True) # with maximum length is 255, and is unique, we don't allow two users use the same eamil address every email address in the DB
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True) # To identity if the user is active or not
    is_staff = models.BooleanField(default=False) # If the user is the staff user, who can access like a admin

    # Specify the model manager and this is use for our custom user model with the Django CLI
    # So Django have to have a custom model manager for the user model so it knows how to create users
    # Django create a instance of UserProfileManager, and did "manager.model = UserProfile"

    # Which means when Django read this, it will run objects.model = UserProfile
    objects = UserProfileManger() # pass in the class - UserProfileManger class

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    # functions: must Specify self as Python default convention
    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email
