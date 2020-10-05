from io import BytesIO
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from django_backend_template.models import Student, InputRecord, Report
from django_backend_template.views.input_file import InputFileView
from django.contrib.auth.models import User


class TestInputFileView(TestCase):
    """Test InputFileView."""

    def setUp(self):
        """."""
        self.factory = APIRequestFactory()

        # Create a sender user
        self.sender = User.objects.create(
            username="asaavedra",
            first_name="Ariel",
            last_name="Saavedra",
            is_superuser=True,
            is_staff=True,
            is_active=True,
            email="adosaa@gmail.com",
            password="dk5c+Pu!E%9jmMK-",
        )
        self.input_file_view = InputFileView.as_view(actions={'post': 'create'})

    def test_creation_request(self):
        """
        Test request an input file created by an admin user, should be SUCCESS
        and also verify if a set of students, input records and reports instances was created
        """
        self.file = BytesIO(b'Student Marco\nStudent David\nStudent Fran\nPresence Marco 1 09:02 10:17 R100\nPresence Marco 3 10:58 12:05 R205\nPresence David 5 14:02 15:46 F505 \n'  )   # in-memory file to upload
        self.file.seek(0)
        body = {
            "input_file": self.file,
        }
        request = self.factory.post(
            '/api/v1/input_file/&format=multipart',
            body
        )
        force_authenticate(request, user=self.sender)
        response = self.input_file_view(request)
        data = response.data
        # Assertions
        self.assertEqual(response.status_code, 201)  # Status HTTP_201
        self.assertTrue(isinstance(data, dict))
        self.assertEqual(len(data), 4)
        self.student1 = Student.objects.get(name="Marco")
        self.student1_record = InputRecord.objects.filter(student=self.student1)
        self.student1_report = Report.objects.get(student=self.student1)
        self.assertIsNotNone(self.student1)
        self.assertIsNotNone(self.student1_report)
        self.assertEqual(len(self.student1_record), 3)
