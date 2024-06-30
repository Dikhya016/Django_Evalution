from django.urls import path
from . import views
urlpatterns = [
    path('userlist/',views.userlist,name='userlist'),
    path('userlist/<int:id>/',views.userdetails,name='userdetails'),
    path('servicelist/',views.servicelist,name='servicelist'),
    path('servicelist/<str:typee>/',views.service_detail,name='service_detail')
]