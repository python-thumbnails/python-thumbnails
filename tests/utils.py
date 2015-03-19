# -*- coding: utf-8 -*-


def has_no_django():
    return not has_django()


def has_django():
    try:
        import django  # noqa isort:skip
        return True
    except ImportError:
        return False
