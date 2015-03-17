# -*- coding: utf-8 -*-


def has_no_django():
    try:
        import django  # noqa isort:skip
        return False
    except ImportError:
        return True
