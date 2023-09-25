
from django.urls import path
from . import views



urlpatterns = [

    path('smsclassifier',views.sms_spam, name = 'smsclassifier'),

]

