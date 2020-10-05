from __future__ import unicode_literals
from django.apps import AppConfig

# =======================================
# Do what needs to be doen in APP config.
# This is a good place to import signals
# =======================================


class DjangoBackendAppConfig(AppConfig):
    name = 'django_backend_template'

    # # If there are signals to be processed (for DB triggers, refer them here)
    def ready(self):
        """."""
        from django_backend_template.signals.student import create_student_report
