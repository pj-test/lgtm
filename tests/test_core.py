import unittest

class LgtmTest(unittest.TestCase):
    def test_lgtm(self):
        from .. import lgtm.core
        self.assertIsNone(lgtm())