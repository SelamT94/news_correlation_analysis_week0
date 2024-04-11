# tests/test_simple.py

import unittest

class TestSimple(unittest.TestCase):
    def test_simple(self):
        print("Running test_simple...")
        self.assertTrue(False, "This assertion should fail")
