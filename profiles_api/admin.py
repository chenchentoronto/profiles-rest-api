from django.contrib import admin
from profiles_api import models

# Register your models here.

# This tells Django admin to register our user profile models with the admin site 
admin.site.register(models.UserProfile)
