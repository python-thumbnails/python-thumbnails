Quickstart
==========

Installation
------------

.. code-block:: bash

    pip install pillow  # default image engine, not necessary if another engine is used
    pip install python-thumbnails

Dependencies
~~~~~~~~~~~~

This project has configurable parts that depends on other modules. In order to
use those the dependencies need to be installed, e.g. to use the ``PillowEngine``
which is the default image engine one has to install pillow.

Usage
-----

Using python-thumbnails can be as little effort as calling ``get_thumbnail``. It
works without configuration, even in Django projects.

.. code-block:: python

    from thumbnails import get_thumbnail

    get_thumbnail('path/to/image.png', '300x300', crop='center')


Configuration
-------------

It is possible to put settings in a Python module and specify it with the
environment variable ``THUMBNAILS_SETTINGS_MODULE``.

Django projects
~~~~~~~~~~~~~~~

The django configuration will be loaded if the environment variable
``DJANGO_SETTINGS_MODULE`` is set. The settings defined in the django
configuration will overwrite the settings from ``THUMBNAILS_SETTINGS_MODULE``.


Flask projects
~~~~~~~~~~~~~~

Use ``THUMBNAILS_SETTINGS_MODULE`` as described above. Better integrations with
Flask is planned in feature versions.
