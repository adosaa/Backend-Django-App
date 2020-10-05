"""
BaseModel Model.

Part of models.core module.
"""

__license__ = "MIT"
__version__ = "0.0.1"
__author__ = "Ariel Saavedra D"
__email__ = "ariel@gmail.com"
__copyright__ = "Copyright 2020"

from django.db import models
import uuid


class BaseModel(models.Model):
    """
    BaseModel abstract model Class.

    An abstract model with all the basic fields for each table in the system.

    :@attr {UUID} id - unique identification for the instance/record.
    :@attr {datetime} created_at - date and time of the record creation.
    :@attr {datetime} updated_at - date and time of the record edition.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

    class Meta:
        """Metadata options for BaseModel."""

        abstract = True
