"""
Student signal methods.

Part of signals.student module
"""

__license__ = "MIT"
__version__ = "0.0.1"
__author__ = "Ariel Saavedra D"
__email__ = "ariel@gmail.com"
__copyright__ = "Copyright 2020"


from django.dispatch import receiver
from django.db.models.signals import post_save
from django_backend_template.models import Student


@receiver(post_save, sender=Student)
def create_student_report(sender, instance, created, **kwargs):
    """
    create_student_report mehtod.

    A method which implements a report creation process per student.

    :@param {Django.model} sender - Django model class which is the signal sender.
    :@param {Django.model instance} instance - Django model instance, which triggered this signal.
    :@param {bool} createdb - boolean that indicates if the instance was created or not.
    :@raises {None}
    :@returns {None}
    """
    if created:
        pass
