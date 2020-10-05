"""
StudentView viewsets Class.

Part of views.student module.
"""

__license__ = "MIT"
__version__ = "0.0.1"
__author__ = "Ariel Saavedra D"
__email__ = "ariel@gmail.com"
__copyright__ = "Copyright 2020"

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
import rest_framework_filters as filters
from django_backend_template.models import Student
from django_backend_template.serializers.student import StudentSerializer
from django_backend_template.controllers.student import StudentController


class StudentFilter(filters.FilterSet):
    """."""

    class Meta:
        """."""

        model = Student
        fields = {
            'created_at': '__all__',
            'updated_at': '__all__',
            'name': '__all__',
        }


class StudentView(viewsets.ModelViewSet):
    """
    Standard model View for save/read/update/delete Student records.

    :@attr {Model Class} model_class - model class of the view
    :@attr {queryset instance} queryset - general queryset from the model
    :@attr {Serializer Class} serializer_class - serializer model of the view
    :@attr {Class} filter_class - filter class per view
    :@attr {tuple} ordering_fields - a tuple with all fields which will be ordering the view
    :@attr {tuple} search_fields - a tuple with all fields which will be search the view
    :@raises {None}
    :@returns {None}
    """

    def __init__(self):
        """."""
        self.model_class = Student
        self.queryset = Student.objects.all()
        self.serializer_class = StudentSerializer
        self.filter_class = StudentFilter
        self.ordering_fields = ('created_at', )
        self.search_fields = ('created_at', )

    def create(self, request, *args, **kwargs):
        """
        Create (POST) method.

        Using a StudentController.create_object_with_params for create Student record.

        :@params {tuple} request - http request of the web requested
        :@raises {APIException}
        :@returns {InputFile instance} created instance of InputFile model.
        """
        created_student = None
        try:
            created_student = StudentController(self.model_class,
                                                self.serializer_class,
                                                request.data).create_object_with_params()
        except Exception as e:
            raise e
        serializer_data = self.serializer_class(created_student).data
        return Response(serializer_data, status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        """
        List (GET) method.

        Using a StudentController.get_entire_collection for list Student records

        :@params {tuple} request - http request of the web requested
        :@raises {APIException}
        :@returns {InputFile list instances} user_profile_list - list of instance of InputFile model.
        """
        student_list = []
        try:
            student_list = StudentController(self.model_class,
                                             self.serializer_class).get_entire_collection()
        except Exception as e:
            raise e
        page = self.paginate_queryset(student_list)
        serializer_data = self.serializer_class(page, many=True).data
        return self.get_paginated_response(serializer_data)
