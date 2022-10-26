from django.contrib import admin
from django.urls import path
from leads.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
]