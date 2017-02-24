#!/usr/bin/python3
import unittest
from tkinter import *

class DefaultWidgetSizeTestCase (unittest.TestCase):
    def runTest(self):
        widget = Widget("test")
        assert widget.size() == (50,50),'incorrect default size'

testcase = DefaultWidgetSizeTestCase()