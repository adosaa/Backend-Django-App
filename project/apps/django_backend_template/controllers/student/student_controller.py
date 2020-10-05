"""
StudentController class.

Part of controllers.student module
"""

__license__ = "MIT"
__version__ = "0.0.1"
__author__ = "Ariel Saavedra D"
__email__ = "ariel@gmail.com"
__copyright__ = "Copyright 2020"

from django_backend_template.controllers.core import ControllerTemplate


class StudentController(ControllerTemplate):
    """
    Services for Student model Class, inherit from ControllerTemplate.

    :@param {Model Class} model - model class of the service
    :@param {Serializer Class} serializer - serializer model of the service
    :@param {dict} params - fields of the instance as a dictionary
    :@param {UUID/string, default=None} instance_id - id of the instance, especially useful in RUD methods
    :@param {List, default=None} extra_fields - list for any type of extra fields.
    :@raises {Exception} params not acceptable
    :@returns {None}
    """

    def __init__(self, model, serializer, params=None, instance_id=None, extra_fields=None):
        """."""
        super(StudentController, self).__init__(model, serializer, params, instance_id, extra_fields)

    def create_object_with_params(self):
        """Declaration of ServiceTemplate's method for instance creation."""
        return super(StudentController, self).create_object_with_params()

    def edit_object_with_params(self):
        """Declaration of ServiceTemplate's method for instance edition."""
        return super(StudentController, self).edit_object_with_params()

    def get_object_with_params(self):
        """Declaration of ServiceTemplate's method for getting instance."""
        return super(StudentController, self).get_object_with_params()

    def get_entire_collection(self):
        """Declaration of ServiceTemplate's method for getting all model's instance."""
        return super(StudentController, self).get_entire_collection()

    def delete_object_with_params(self):
        """Declaration of ServiceTemplate's method for delete instance."""
        return super(StudentController, self).delete_object_with_params()
