# python-thumbnails  [![Build status](https://ci.frigg.io/badges/relekang/python-thumbnails/)](https://ci.frigg.io/relekang/python-thumbnails/last/) [![Coverage status](https://ci.frigg.io/badges/coverage/relekang/python-thumbnails/)](https://ci.frigg.io/relekang/python-thumbnails/last/)

[![Join the chat at https://gitter.im/relekang/python-thumbnails](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/relekang/python-thumbnails?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Thumbnails for Django, Flask and other Python projects.

## Work in progress
This project is currently work in progress. It is not production ready.
[This gist](https://gist.github.com/relekang/1544815ce1370a0be2b4) outlines the planned features
and the status of them.

## Install
```bash
pip install pillow  # default image engine, not necessary if another engine is used
pip install python-thumbnails
```

## Usage

```python
from thumbnails import get_thumbnail

get_thumbnail('path/to/image.png', '300x300', 'center')
```

----------------------

MIT © Rolf Erik Lekang
