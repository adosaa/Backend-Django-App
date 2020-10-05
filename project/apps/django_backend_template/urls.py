from django.urls import path, include
from django_backend_template.routers.student import urls as student_urls

urlpatterns = [
    path('student/', include(student_urls)),
]
