import time
from django.test import TestCase
from django.core.cache import get_cache

class InfiniteMemcached(TestCase):
    def test_handle_timeouts(self):
        mc = get_cache('infinite_memcached.cache.MemcachedCache',
                       LOCATION='127.0.0.1:11211')

        self.assertEqual(0, mc._get_memcache_timeout(0))
        self.assertEqual(60, mc._get_memcache_timeout(60))
        self.assertEqual(300, mc._get_memcache_timeout(None))

        # For timeouts over 30 days, the expire time is stored as a
        # UNIX timestamp. Just make sure that happens.
        sixty_days = (60*60*24*60)
        self.assertEqual(int(time.time() + sixty_days),
                         mc._get_memcache_timeout(sixty_days))
