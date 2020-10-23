#!/usr/bin/env python3
"""
    Testing WorldVisualizer Module
    ============================

    Each and every method must have its designated test.

"""

import os
import sys
import unittest as ut

sys.path.append("../")

import WorldVisualizer

class test_WorldVisualizer(ut.TestCase):
    def setUp(self):
        self._root = os.path.dirname(__file__)
