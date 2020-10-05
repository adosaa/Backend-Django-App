from django.test import TestCase
from unittest.mock import patch
from django_backend_template.controllers.core import ControllerTemplate
from django_backend_template.serializers.student import StudentSerializer
from django_backend_template.models import Student


class TestControllerTemplate(TestCase):
    """Test core service ControllerTemplate."""

    def setUp(self):
        """Initialize test."""
        self.student1 = Student.objects.create(
            name="Ariel"
        )

    @patch.multiple(ControllerTemplate, __abstractmethods__=set())
    def test_abstract_class_creation(self):
        """Test Create Succeeds."""
        self.student_info = {
            "name": "Rodolfo"
        }
        self.service_template = ControllerTemplate(Student, StudentSerializer,
                                                   self.student_info)
        self.student_created = self.service_template.create_object_with_params()
        self.assertIsNotNone(self.student_created)
        self.assertEqual(self.student_created.name, "Rodolfo")

    @patch.multiple(ControllerTemplate, __abstractmethods__=set())
    def test_abstract_class_get(self):
        """Test Getting Succeeds."""
        self.service_template = ControllerTemplate(Student, StudentSerializer,
                                                   instance_id=self.student1.id)
        self.get_student = self.service_template.get_object_with_params()
        self.assertIsNotNone(self.get_student)
        self.assertEqual(self.get_student.name, "Ariel")

    @patch.multiple(ControllerTemplate, __abstractmethods__=set())
    def test_abstract_class_edit(self):
        """Test Edition Succeeds."""
        self.student_info = {
            "name": "Ariela"
        }
        self.service_template = ControllerTemplate(Student, StudentSerializer,
                                                   params=self.student_info,
                                                   instance_id=self.student1.id)
        self.edited_student = self.service_template.edit_object_with_params()
        self.assertIsNotNone(self.edited_student)
        self.assertEqual(self.edited_student.name, "Ariela")

    @patch.multiple(ControllerTemplate, __abstractmethods__=set())
    def test_abstract_class_delete(self):
        """Test delete Succeeds."""
        self.service_template = ControllerTemplate(Student, StudentSerializer,
                                                   instance_id=self.student1.id)
        self.delete_student = self.service_template.delete_object_with_params()
        self.assertIsNotNone(self.delete_student)
        self.assertEqual(self.delete_student, 200)
