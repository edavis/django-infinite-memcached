**UPDATE (November 30, 2021):** You probably don't need to use this. Django now officially supports `cache keys that never expire <https://docs.djangoproject.com/en/3.2/topics/cache/#cache-arguments>`_.

----

django-infinite-memcached
=========================

A Django memcached backend to handle "infinite" timeouts (i.e., never
expire an item).

Installation
-------------

1) ``$ pip install django-infinite-memcached``

2) Set ``infinite_memcached.cache.MemcachedCache`` as your cache backend::

    CACHES = {
        "default": {
            "BACKEND": "infinite_memcached.cache.MemcachedCache",
            "LOCATION": "127.0.0.1:11211",
        },
    }

How to use
----------

Either set the ``TIMEOUT`` option to 0::

    CACHES = {
        "default": {
            "BACKEND": "infinite_memcached.cache.MemcachedCache",
            "LOCATION": "127.0.0.1:11211",
            "TIMEOUT": 0,
        },
    }

Or pass ``timeout=0`` to the `low-level cache commands
<https://docs.djangoproject.com/en/1.4/topics/cache/#the-low-level-cache-api>`_
(e.g., set, add, etc.) to keep things from expiring.

Why?
----

Django's default memcached backend doesn't accept timeout values of
zero, instead using the default timeout (five minutes) when zero is passed.

This cache backend overrides how timeouts are calculated so any
timeout of zero is passed directly to memcached, telling memcached to
never expire an item.

This has been an `known issue
<https://code.djangoproject.com/ticket/9595>`_ for awhile, but
concerns over backwards compatibility have prevented any fixes from
taking place.

Tests
-----

The README in test_project/ has instructions on running the test suite.

.. image:: https://secure.travis-ci.org/edavis/django-infinite-memcached.png
   :target: https://travis-ci.org/edavis/django-infinite-memcached

License
-------

BSD. See LICENSE.txt.
