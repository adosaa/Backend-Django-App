"""
StudentSerializer Serializer.

Part of serializer.report module.
"""

__license__ = "MIT"
__version__ = "0.0.1"
__author__ = "Ariel Saavedra D"
__email__ = "ariel@gmail.com"
__copyright__ = "Copyright 2020"

from rest_framework import serializers
from django_backend_template.models import Student


class StudentSerializer(serializers.ModelSerializer):
    """
    Serializer class for Student Model.

    :@param {all} all - all the Student fields serialized.
    :@raises {None}
    :@returns {None}
    """

    class Meta:
        model = Student
        fields = '__all__'
