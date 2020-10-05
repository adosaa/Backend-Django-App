"""
wait_and_process_transaction method.

Part of utils.db_tools module.
"""

__license__ = "MIT"
__version__ = "0.0.1"
__author__ = "Ariel Saavedra D"
__email__ = "ariel@gmail.com"
__copyright__ = "Copyright 2020"


import time
from random import random
from functools import wraps

try:
    from django.db import transaction
except Exception as e:
    print(e)


def wait_and_process_transaction(max_tries=5):
    """
    wait_and_process_transaction decorator Method.

    Function That applies a standard workflow to wait and execute sql statement in a transaction.
    Note this functionality assumes django and DRF is installed.

    :@attr {Integer, default=5} max_tries - amounts of attempts.
    :@raises {ValidationError|APIException} raised from processor function.
    :@returns {None} processor - result of envolved function.
    """
    def wait_and_process_transaction_decorator(method):

        @wraps(method)
        def processor(*args, **kwargs):
            # This should be assigned to different variable to avoid scope issues
            total_tries = max_tries if max_tries > 1 else 1
            num_tries = 0
            updated = False
            try_exception = None
            while num_tries < total_tries:
                try:
                    with transaction.atomic():
                        result = method(*args, **kwargs)
                        return result
                    # NOTE Important to break of transaction id succwssful
                    updated = True
                    break
                except Exception as e:
                    num_tries = num_tries + 1
                    try_exception = e
                    print("Trouble executing '%s', Num Tries: %d." % (method.__name__, num_tries), e)
                    time.sleep(random())

            if not updated and try_exception is not None:
                print("Failed. Unable to execute '%s', Aborting after %d tries" % (method.__name__, max_tries))
                raise try_exception
        return processor
    return wait_and_process_transaction_decorator
