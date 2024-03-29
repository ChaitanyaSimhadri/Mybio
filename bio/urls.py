
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name ="home"),
    path('predict/',views.predict, name = 'predict'),
    path('contact', views.contact,name = 'contact'),
    path('blog/',views.blog, name = 'blog'),
    path('download/<str:file_name>/', views.DownloadFileView.as_view(), name='download_file'),



]

handler404 = views.error_404_view