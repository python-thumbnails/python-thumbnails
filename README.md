# python-thumbnails [![CircleCI](https://circleci.com/gh/python-thumbnails/python-thumbnails.svg?style=svg&circle-token=4e9cc99497f1c2901ceb06cd716eb124c8c27837)](https://circleci.com/gh/python-thumbnails/python-thumbnails)

Thumbnails for Django, Flask and other Python projects.

[![Documentation Status](https://readthedocs.org/projects/python-thumbnails/badge/?version=latest)](https://readthedocs.org/projects/python-thumbnails/?badge=latest)
[![Join the chat at https://gitter.im/relekang/python-thumbnails](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/relekang/python-thumbnails?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

## Install
```bash
pip install pillow  # default image engine, not necessary if another engine is used
pip install python-thumbnails
```

## Usage

```python
from thumbnails import get_thumbnail

get_thumbnail('path/to/image.png', '300x300', crop='center')
```

----------------------

MIT © Rolf Erik Lekang
