from django.core.cache.backends import memcached

class MemcachedCache(memcached.MemcachedCache):
    def _get_memcache_timeout(self, timeout):
        """
        Allow zero to be passed as a timeout to memcached.

        Django's default MemcachedCache cache backend doesn't accept
        zeroes as a timeout value. When passed a zero (i.e., never
        expire), it instead uses the default timeout of five minutes.

        When using this cache backend, timeouts of zero are passed
        along to memcached and any other value is passed to Django's
        MemcachedCache cache backend.
        """
        if timeout == 0:
            return 0
        else:
            return super(MemcachedCache, self)._get_memcache_timeout(timeout)
