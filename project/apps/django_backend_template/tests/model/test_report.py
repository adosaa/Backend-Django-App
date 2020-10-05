from django.test import TestCase
from datetime import time
from django_backend_template.models import Student, Report, InputRecord, InputFile


class TestReport(TestCase):
    """Test model Report."""

    def setUp(self):
        """Initialize test."""
        self.student1 = Student.objects.create(
            name="Ariel"
        )

        self.student2 = Student.objects.create(
            name="Jose"
        )

        self.file = InputFile.objects.create(
            content="Presence Marco 1 09:02 10:17 R100"
        )

        self.start_time = time(9, 2)
        self.end_time = time(10, 17)
        self.student2_record = InputRecord.objects.create(
            input_file=self.file,
            command="presence", student=self.student2,
            days=1, start_time=self.start_time,
            end_time=self.end_time, classroom_code="R100"
        )

    def test_create_succeeds(self):
        """Test Create Succeeds."""
        self.assertIsNotNone(self.student2_record)
        self.student_report = Report.objects.get(student=self.student2)
        self.assertEqual(self.student_report.student.name, "Jose")
        self.assertEqual(self.student2_record.command, "presence")
        self.assertEqual(self.student_report.days, 1)

    def test_str_verification(self):
        """Test str method."""
        self.assertIsNotNone(self.student1)
        self.student_report1 = Report.objects.get(student=self.student1)
        self.student_report2 = Report.objects.get(student=self.student2)
        self.assertEqual(self.student_report1.student.name, "Ariel")
        self.assertEqual(self.student_report1.days, 0)
        self.assertEqual(str(self.student_report1), 'Ariel: 0 minutes')
        self.assertEqual(str(self.student_report2), 'Jose: 75 minutes in 1 day')
