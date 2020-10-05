"""
Student router urls.

Part of routers.student module.
"""


from django.urls import path
from django_backend_template.views import student

urlpatterns = [
    path('', student.StudentView.as_view({
        'post': 'create',
        'get': 'list',
    }), name='student')
]
