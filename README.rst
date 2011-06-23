django-infinite-memcached
=========================

A cache backend to better work with "infinite" timeouts in memcached.

Enables the use of ``timeout=0`` when using memcached in Django.

Installation
-------------

1) ``pip install -e git+http://github.com/edavis/django-infinite-memcached.git#egg=django-infinite-memcached``

2) Set ``infinite_memcached.MemcachedCache`` as the ``BACKEND`` in ``CACHES``

For example::

    CACHES = {
        "default": {
            "BACKEND": "infinite_memcached.MemcachedCache",
            "LOCATION": "127.0.0.1:11211",
        },
    }

This cache backend only overrides how timeouts are calculated, so
existing code should continue to work.  You'll just now be able to use
``timeout=0`` with ``cache.add``, ``cache.set``, and ``cache.set_many``.

Versions
--------

Tested with:

- Django 1.3
- python-memcached 1.47
- memcached 1.4.5

TODO
----

- Add unittests
- Add support for pylibmc
- Contributions welcome
