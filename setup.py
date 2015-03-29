from setuptools import setup, find_packages


def _read_long_description():
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst', format='markdown')
    except Exception:
        return None


setup(
    name='python-thumbnails',
    version='0.4.1',
    url='http://github.com/relekang/python-thumbnails',
    author='Rolf Erik Lekang',
    author_email='me@rolflekang.com',
    description='Thumbnails for Django, Flask and other Python projects.',
    long_description=_read_long_description(),
    packages=find_packages(exclude='tests'),
    license='MIT',
    install_requires=[
        'six',
        'requests'
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ]
)
