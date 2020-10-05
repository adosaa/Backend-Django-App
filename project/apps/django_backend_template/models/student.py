"""
Student Model.

Part of models module.
"""

__license__ = "MIT"
__version__ = "0.0.1"
__author__ = "Ariel Saavedra D"
__email__ = "ariel@gmail.com"
__copyright__ = "Copyright 2020"

from django.db import models
from django_backend_template.models.core import BaseModel


class Student(BaseModel):
    """
    Student Model.

    A model that has the responsibility to save and maintain student's information.
    it's assumed that by the lack of a real way to identify the uniqueness between
    each student, the name will be not-repeatable.

    :@attr {UUID} id - unique identification for the instance/record (inherited from BaseModel).
    :@attr {String} name - name of the instance.
    :@attr {datetime} created_at - date and time of the record creation (inherited from BaseModel).
    :@attr {datetime} updated_at - date and time of the record edition (inherited from BaseModel).
    """

    name = models.CharField(max_length=20, unique=True, blank=False, null=False)

    class Meta:
        """Metadata options for Student."""

        verbose_name_plural = 'students'
        app_label = 'django_backend_template'
