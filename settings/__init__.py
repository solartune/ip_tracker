from django.core.exceptions import ImproperlyConfigured

try:
    from .local import *
except ImportError:
    import os
    path = os.path.relpath(os.path.dirname(__file__))
    message = """
    You MUST **review** the appropriate environment specific
    configuration in the local settings module:

        (venv)$ cp {path}/local_sample.py {path}/local.py
        (venv)$ $EDITOR {path}/local.py
    """

    raise ImproperlyConfigured(message.format(path=path))
