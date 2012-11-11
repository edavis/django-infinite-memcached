django-infinite-memcached
=========================

A Django memcached backend to handle "infinite" timeouts (i.e., never
expire an item).

Installation
-------------

1) ``pip install django-infinite-memcached``

2) Set ``infinite_memcached.cache.MemcachedCache`` as your cache backend::

    CACHES = {
        "default": {
            "BACKEND": "infinite_memcached.cache.MemcachedCache",
            "LOCATION": "127.0.0.1:11211",
        },
    }

Why is this needed?
-------------------

Django's default memcached backend doesn't accept timeout values of
zero, instead using the default timeout (five minutes) when zero is passed.

This cache backend overrides how timeouts are calculated so any
timeout of zero is passed directly to memcached, telling memcached to
never expire an item.

This has been an `known issue
<https://code.djangoproject.com/ticket/9595>`_ for awhile, but
concerns over backwards compatibility have prevented any fixes from
taking place.

License
-------

BSD
