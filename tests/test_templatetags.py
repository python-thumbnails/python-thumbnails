# -*- coding: utf-8 -*-
import unittest

from .compat import mock
from .utils import has_installed

try:
    from django.template import Context, Template
    from django.db.models.fields import files
except ImportError:
    pass


@unittest.skipIf(not has_installed('django'), 'Django not installed')
class TemplateTagTestCase(unittest.TestCase):

    @mock.patch('thumbnails.get_thumbnail')
    def test_get_thumbnail_templatetag(self, mock_get_thumbnail):
        Template(
            '{% load thumbnails %}{% get_thumbnail "static/image.jpg" "200" as im %}{{im.url}}',
        ).render(Context())

        mock_get_thumbnail.assert_called_once_with('static/image.jpg', '200')

    @mock.patch('thumbnails.get_thumbnail')
    def test_get_thumbnail_templatetag_with_kwarg(self, mock_get_thumbnail):
        Template(
            '{% load thumbnails %}'
            '{% get_thumbnail "static/image.jpg" "100x100" crop="center" as im %}{{im.url}}',
        ).render(Context())

        mock_get_thumbnail.assert_called_once_with('static/image.jpg', '100x100', crop='center')

    @mock.patch('thumbnails.get_thumbnail')
    def test_get_thumbnail_templatetag_with_multiple_kwargs(self, mock_get_thumbnail):
        Template(
            '{% load thumbnails %}'
            '{% get_thumbnail "static/image.jpg" "200x200" crop="center" scale_up=True as im %}'
            '{{im.url}}',
        ).render(Context())

        mock_get_thumbnail.assert_called_once_with('static/image.jpg', '200x200', crop='center',
                                                   scale_up=True)

    @mock.patch('thumbnails.get_thumbnail')
    def test_get_thumbnail_templatetag_with_FileField_as_source(self, mock_get_thumbnail):
        field = files.FileField()
        _file = files.FieldFile(field=field, instance=None, name='image.jpg')
        Template(
            '{% load thumbnails %}'
            '{% get_thumbnail image "200x200" as im %}'
            '{{im.url}}',
        ).render(Context({
            'image': _file
        }))

        mock_get_thumbnail.assert_called_once_with(_file, '200x200')
