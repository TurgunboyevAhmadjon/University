from django.contrib import admin
from django.urls import path
from courses.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fan/', fan),
    path('oqituvchilar/', teacher),
    path('oqituvchi/<int:pk>/', teacher_del),
    path('teacher/<int:pk>/edit/', teacher_edit),
    path('yonalishlar/', speciality),
    path('yonalish/<int:pk>/', speciality_del),
    path('yonalishlar/<int:pk>/edit/', speciality_edit),
]
