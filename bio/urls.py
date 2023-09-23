
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name ="home"),
    path('predict/',views.predict, name = 'predict'),
    path('contact', views.contact,name = 'contact'),
    path('download/<str:file_name>/', views.DownloadFileView.as_view(), name='download_file'),


]
