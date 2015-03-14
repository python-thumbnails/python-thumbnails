from setuptools import setup

import thumbnails


def _read_long_description():
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst', format='markdown')
    except Exception:
        return None


setup(
    name='python-thumbnails',
    version=thumbnails.__version__,
    url='http://github.com/relekang/python-thumbnails',
    author='Rolf Erik Lekang',
    author_email='me@rolflekang.com',
    description='Thumbnails for Django, Flask and other Python projects.',
    long_description=_read_long_description(),
    py_modules=['thumbnails'],
    license='MIT',
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ]
)
