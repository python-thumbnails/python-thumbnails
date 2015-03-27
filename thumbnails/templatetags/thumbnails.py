# -*- coding: utf-8 -*-
from __future__ import absolute_import

import re

from django import template
from django.template import Library
from django.template.base import TemplateSyntaxError

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
