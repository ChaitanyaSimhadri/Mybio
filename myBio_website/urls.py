
from django.contrib import admin
from django.urls import path, include


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('bio.urls')),
    path('',include('SMS_Classifier.urls')),
    


]
