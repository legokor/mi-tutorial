from unittest import TestCase, skip

class TryTesting(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

    @skip("This would fail")
    def test_always_fails(self):
        self.assertTrue(False)
