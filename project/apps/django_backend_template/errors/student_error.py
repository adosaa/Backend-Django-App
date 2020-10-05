"""
Student error's list.

part of errors module.
"""

__license__ = "MIT"
__version__ = "0.0.1"
__author__ = "Ariel Saavedra D"
__email__ = "ariel@gmail.com"
__copyright__ = "Copyright 2020"

from rest_framework.exceptions import APIException


class StudentBadRequest(APIException):
    status_code = 400
    default_detail = 'Malformed request or bad parameters when requesting Student record(s)'
    default_code = 'student_bad_request'


class StudentServerError(APIException):
    status_code = 500
    default_detail = 'Error in some procedures of Student Logic, please try again.'
    default_code = 'student_server_error'


class StudentNotFound(APIException):
    status_code = 404
    default_detail = 'Student record not found'
    default_code = 'student_not_found'


class StudentNotAccetable(APIException):
    status_code = 406
    default_detail = 'Student record not Acceptable'
    default_code = 'student_not_acceptable'
