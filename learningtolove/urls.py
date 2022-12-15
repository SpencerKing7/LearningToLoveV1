"""
Definition of urls for learningtolove.
"""

from datetime import datetime
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
]
