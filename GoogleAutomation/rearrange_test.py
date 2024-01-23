#!/usr/bin/env python3
from rearrange import rearrange_name
import unittest
class TestRearrange(unittest.TestCase):
    def test_basic(self):
        test_input = "Lovelace, Ada"
        expected_output = "Ada Lovelace"
        self.assertEqual(rearrange_name(test_input),expected_output)
    def test_empty(self):
        test_input = ""
        expected_output = ""
        self.assertEqual(rearrange_name(test_input),expected_output)
    def test_invalid(self):
        self.assertRaises(ValueError,rearrange_name,"[]",-1)


unittest.main()
