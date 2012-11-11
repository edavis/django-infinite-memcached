from django.core.cache.backends import memcached

class MemcachedCache(memcached.MemcachedCache):
    def _get_memcache_timeout(self, timeout):
        """Override _get_memcache_timeout so that it accepts 0."""
        if timeout == 0: return 0
        else: return super(MemcachedCache, self)._get_memcache_timeout(timeout)
