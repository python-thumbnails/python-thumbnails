Creating thumbnails
-------------------

``thumbnails.get_thumbnail`` should be used to generate thumbnails from python code. It takes the
original image and size is positional arguments and needs to be passed each time the function is
called. Other options can be passed as keyword arguments. The available options is listed below:


.. autofunction:: thumbnails.get_thumbnail


Django specific features
~~~~~~~~~~~~~~~~~~~~~~~~

Templatetags
^^^^^^^^^^^^

**get_thumbnail**

This templatetag is a shortcut for ``thumbnails.get_thumbnail``, thus all arguments and keyword
arguments are the same as described in the section above. It is necessary to define the variable
name for the thumbnail with an ``as`` keyword as shown in the example below.

.. code-block:: html+django

    {% load thumbnails %}

    {% get_thumbnail "image.jpg" "400x400" crop="center" as thumbnail %}
    <img src="{{ thumbnail.url }}" alt="The thumbnail" style="width: {{ thumbnail.width }} />


Filters
^^^^^^^

.. autofunction:: thumbnails.templatetags.thumbnails.markdown_thumbnails

.. code-block:: html+django

    {% load thumbnails %}

    {{ content|markdown_thumbnails }}

.. autofunction:: thumbnails.templatetags.thumbnails.html_thumbnails

.. code-block:: html+django

    {% load thumbnails %}

    {{ content|html_thumbnails }}

.. autofunction:: thumbnails.templatetags.thumbnails.safe_html_thumbnails

.. code-block:: html+django

    {% load thumbnails %}

    {{ content|safe_html_thumbnails }}

**Creating custom text filters**

It is possible to create custom text filters by utilizing the ``text_filter`` function described
below.

.. autofunction:: thumbnails.templatetags.thumbnails.text_filter

Below is the code for the ``html_thumbnails``-filter shown as an example of how to use
``text_filter``.

.. code-block:: python

    @register.filter
    def html_thumbnails(value):
        return mark_safe(text_filter('<img(?: alt="(%(caption)s)?")? src="(%(image)s)"', value))
