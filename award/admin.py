from django.contrib import admin
from .models import Posts,Ratings,UserProfile

# Register your models here.

admin.site.register(Posts)
admin.site.register(Ratings)
admin.site.register(UserProfile)