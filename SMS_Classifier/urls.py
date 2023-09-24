
from django.urls import path
from . import views
from bio.views import error_404_view



urlpatterns = [

    path('smsclassifier',views.sms_spam, name = 'smsclassifier'),

]

