from django.contrib import admin
from .models import jobOpenings, accounts


admin.site.register(jobOpenings, accounts)