from django.test import TestCase
from django_backend_template.models import Student, Report


class TestStudent(TestCase):
    """Test model Student."""

    def setUp(self):
        """Initialize test."""
        self.student1 = Student.objects.create(
            name="Ariel"
        )

    def test_create_succeeds(self):
        """Test Create Succeeds."""
        self.assertIsNotNone(self.student1)
        self.student_report = Report.objects.get(student=self.student1)
        self.assertEqual(self.student1.name, "Ariel")
        self.assertIsNotNone(self.student_report)
        self.assertEqual(self.student_report.student.name, "Ariel")

    def test_creation_fail_due_bad_tuple(self):
        """Test Failed based on a same name student creation."""
        with self.assertRaises(Exception):
            self.student2 = Student.objects.create(
                name="Ariel"
            )
