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

This project integrates with Django without any specific configuration, put your thumbnails settings
within your Django settings and you should be good to go. However, if you want to use the
templatetag it is necessary to add ``thumbnails`` to installed apps:

.. code-block:: python

    INSTALLED_APPS = (
        # your other apps

        'thumbnails',
    )



Flask projects
~~~~~~~~~~~~~~

Use ``THUMBNAILS_SETTINGS_MODULE`` as described above. Better integrations with
Flask is planned in feature versions.
