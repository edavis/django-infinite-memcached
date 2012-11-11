from django.test import TestCase

class InfiniteMemcached(TestCase):
    def test_foo(self):
        self.assertEqual(4, 2+2)
