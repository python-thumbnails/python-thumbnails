# -*- coding: utf-8 -*-


def has_no_django():
    try:
        import django
        return False
    except ImportError:
        return True
