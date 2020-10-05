"""
ControllerTemplate class.

Part of controllers.core module
"""

__license__ = "MIT"
__version__ = "0.0.1"
__author__ = "Ariel Saavedra D"
__email__ = "ariel@gmail.com"
__copyright__ = "Copyright 2020"

from rest_framework import status
from abc import ABCMeta, abstractmethod
from django_backend_template.utils.db_tools.transactional import wait_and_process_transaction
from django_backend_template import errors


class ControllerTemplate(metaclass=ABCMeta):
    """
    Abstract class for every service per Model (especially for complex models).

    This class was design following the abstract class pattern according to DRY principle
    and adding CRUD methods for a easy instances access/management. Once this class is
    inherit, their methods must be added and overload if is necessary.

    :@param {Model Class} model - model class of the service
    :@param {Serializer Class} serializer - serializer model of the service
    :@param {dict, default=None} params - fields of the instance as a dictionary
    :@param {UUID/string, default=None} instance_id - id of the instance, especially useful in GET-EDIT-DELETE methods
    :@returns {None}
    """

    def __init__(self, model, serializer, params=None, instance_id=None, extra_fields=None):
        """."""
        self.model = model
        self.serializer = serializer
        self.params = params
        self.instance_id = instance_id
        self.extra_fields = extra_fields

    @abstractmethod
    @wait_and_process_transaction(max_tries=2)
    def create_object_with_params(self):
        """
        Basic (Transactional) method for create a instance of the self.model.

        :@raises {APIException} ModelBadRequest - 400 malformed request
        :@returns {Model Instance} - instance of the model
        """
        try:
            serializer = self.serializer(data=self.params)
            if serializer.is_valid():
                return serializer.save()
            else:
                exception_path = "errors.%s_error.%sBadRequest" % (self.model.__name__.lower(),
                                                                   self.model.__name__)
                raise eval(exception_path)
        except Exception as e:
            raise e

    @abstractmethod
    @wait_and_process_transaction(max_tries=2)
    def get_entire_collection(self):
        """
        Basic method for get all collection from certain model

        :@raises {APIException} ModelBadRequest - 400 malformed request
        :@returns {Model Instance} - instance of the model
        """
        try:
            return self.model.objects.all()
        except Exception:
            exception_path = "errors.%s_error.%sServerError" % (self.model.__name__.lower(), self.model.__name__)
            raise eval(exception_path)

    @abstractmethod
    def get_object_with_params(self):
        """
        Basic method for get a instance of the self.model.

        :@raises {APIException} ModelNotFound - 404 record not found
        :@returns {Model Instance} - instance of the model
        """
        try:
            return self.model.objects.get(id=self.instance_id)
        except Exception:
            exception_path = "errors.%s_error.%sNotFound" % (self.model.__name__.lower(), self.model.__name__)
            raise eval(exception_path)

    @abstractmethod
    @wait_and_process_transaction(max_tries=2)
    def edit_object_with_params(self):
        """
        Basic (Transactional) method for edit a instance of the self.model.

        :@raises {APIException} ModelBadRequest - 400 malformed request
        :@returns {Model Instance} - instance of the model
        """
        try:
            model_instance = self.get_object_with_params()
            serializer = self.serializer(model_instance, data=self.params, partial=True)
            if serializer.is_valid():
                return serializer.save()
            else:
                exception_path = "errors.%s_error.%sBadRequest" % (self.model.__name__.lower(), self.model.__name__)
                raise eval(exception_path)
        except Exception as e:
            raise e

    @abstractmethod
    @wait_and_process_transaction(max_tries=2)
    def delete_object_with_params(self):
        """
        Basic (Transactional) method for delete a instance of the self.model.

        :@raises {APIException} ModelBadRequest - 400 malformed request
        :@returns {HTTP code} - 200 OK
        """
        try:
            self.get_object_with_params().delete()
            return status.HTTP_200_OK
        except Exception:
            exception_path = "errors.%s_error.%sBadRequest" % (self.model.__name__.lower(), self.model.__name__)
            raise eval(exception_path)
