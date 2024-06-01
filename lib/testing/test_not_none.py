#!/usr/bin/env python3

import unittest
from not_none_functions import return_not_none

class TestNotNoneFunction(unittest.TestCase):
    def test_return_not_none(self):
        result = return_not_none()
        self.assertIsNotNone(result, "The return_not_none function should not return None")

if __name__ == '__main__':
    unittest.main()
