#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import json
import sys

if __name__ == "__main__":

    environment = "local"

    settings = os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.' + environment)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)
    os.environ.setdefault("ENV", environment)

    if environment == 'local':
        os.environ.setdefault("ENV", environment)
    else:
        with open("zappa_settings.json") as zappa_settings_file:
            data = json.load(zappa_settings_file)
            zappa_variables = data[environment]['environment_variables']
        for zappa_variable in zappa_variables:
            os.environ.setdefault(zappa_variable, zappa_variables[zappa_variable])

    if 'test' in sys.argv:
        import coverage
        cov = coverage.coverage()
        cov.erase()
        cov.start()

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    if 'test' in sys.argv:
        cov.stop()
        cov.save()
        cov.report()
