# -*- coding: utf-8 -*-
from __future__ import absolute_import

import re

from django import template
from django.template import Library
from django.template.base import TemplateSyntaxError
from django.utils.safestring import mark_safe

from thumbnails import settings

register = Library()


@register.tag(name='get_thumbnail')
class ThumbnailNode(template.Node):

    variable_name = None

    def __init__(self, parser, token):
        tokens = token.split_contents()
        self.original = parser.compile_filter(tokens[1])
        self.size = parser.compile_filter(tokens[2])
        self.options = {}

        if tokens[-2] == 'as':
            self.variable_name = tokens[-1]
        else:
            raise TemplateSyntaxError('get_thumbnail tag needs an variable assignment with "as"')

        for option in tokens[3:-2]:
            parsed_option = re.match(r'^(?P<key>[\w]+)=(?P<value>.+)$', option.strip())
            if parsed_option:
                key = parsed_option.group('key')
                value = parser.compile_filter(parsed_option.group('value'))
                self.options[key] = value
            else:
                raise TemplateSyntaxError('{} is invalid option syntax'.format(option))

    def render(self, context):
        from thumbnails import get_thumbnail  # imported inline in order for mocking to work
        if self.original and self.size:
            original = self.original.resolve(context)
            size = self.size.resolve(context)
            options = {}
            for key in self.options:
                options[key] = self.options[key].resolve(context)

            context[self.variable_name] = get_thumbnail(original, size, **options)
        else:
            raise TemplateSyntaxError()

        return ''


def text_filter(regex_base, value):
    """
    A text-filter helper, used in ``markdown_thumbnails``-filter and ``html_thumbnails``-filter.
    It can be used to build custom thumbnail text-filters.

    :param regex_base: A string with a regex that contains ``%(captions)s`` and ``%(image)s`` where
                       the caption and image should be.
    :param value: String of text in which the source URLs can be found.
    :return: A string ready to be put in a template.
    """
    from thumbnails import get_thumbnail
    regex = regex_base % {
        'caption': '[a-zA-Z0-9\.\,:;/_ \(\)\-\!\?\"]+',
        'image': '[a-zA-Z0-9\.:/_\-\% ]+'
    }
    images = re.findall(regex, value)

    for i in images:
        image_url = i[1]
        image = get_thumbnail(
            image_url,
            **settings.THUMBNAIL_FILTER_OPTIONS
        )
        value = value.replace(i[1], image.url)

    return value


@register.filter
def markdown_thumbnails(value):
    """
    Markdown filter that replaces all images with thumbnails.
    """
    return text_filter('!\[(%(caption)s)?\][ ]?\((%(image)s)\)', value)


@register.filter
def safe_html_thumbnails(value):
    """
    HTML filter that replaces all images with thumbnails, the returned string is not marked as safe.
    """
    return text_filter('<img(?: alt="(%(caption)s)?")? src="(%(image)s)"', value)


@register.filter
def html_thumbnails(value):
    """
    HTML filter that replaces all images with thumbnails, the returned string is marked as safe.
    """
    return mark_safe(text_filter('<img(?: alt="(%(caption)s)?")? src="(%(image)s)"', value))
