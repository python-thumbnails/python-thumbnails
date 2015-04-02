Contributions are highly appreciated, please follow the following guidelines in order to make the
process of including the contributions easier.

It sums up to write tests, follow pep8 and the import-sorting guidelines. New features
needs to be documented.

Adding features
~~~~~~~~~~~~~~~

Adding an engine
^^^^^^^^^^^^^^^^

If you are adding a new engine there is already a test-case ready that you should use to test your
new engine. In ``tests.test_engine`` there is a EngineTestMixin that you should add to your test
case. Remember to set the ``ENGINE`` attribute. If your engine has their own dependencies it is
necessary to decorate the test class with
``@unittest.skipIf(not has_dependency(), 'Dependency not installed')``. The ``has_dependency``
function should be created in ``test.utils``. There exist some in the code base already so look there
for examples.

Below is the test case for the PillowEngine. It is a good example of how to add tests for a new
engine.

.. code-block:: python

    @unittest.skipIf(not has_installed('pillow'), 'Pillow not installed')
    class PillowEngineTestCase(EngineTestMixin, unittest.TestCase):
        ENGINE = PillowEngine

Adding a cache backend
^^^^^^^^^^^^^^^^^^^^^^

As with the image engines, cache backends has a test mixin that should be used when a new cache
backend is created. Example usage of the test mixin is shown below.

.. code-block:: python

    class SimpleCacheBackendTestCase(CacheBackendTestMixin, unittest.TestCase):
        BACKEND = SimpleCacheBackend

