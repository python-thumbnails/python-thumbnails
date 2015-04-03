# -*- coding: utf-8 -*-
import thumbnails
from tests import data
from thumbnails.conf import settings

URL = 'https://unsplash.imgix.net/photo-1422405153578-4bd676b19036?q=75&fm=jpg&' \
      's=5ecc4c704ea97d85ea550f84a1499228'

print(settings.THUMBNAIL_PATH)

print(thumbnails.get_thumbnail(URL, '800x800').url)
print(thumbnails.get_thumbnail(URL, '800').url)
print(thumbnails.get_thumbnail(URL, 'x800').url)
print(thumbnails.get_thumbnail(URL, '400x400', crop='center').url)
print(thumbnails.get_thumbnail(URL, '400x400', crop='top').url)
print(thumbnails.get_thumbnail(URL, '400x400', crop='left').url)
print(thumbnails.get_thumbnail(data.BASE64_STRING_OF_IMAGE, '200x200', crop='center').url)
