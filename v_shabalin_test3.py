from unittest import TestCase

__author__ = 'v_shabalin'

class TestDemoFeature(TestCase):
    def test_some_feature_empty(self):
        pass

    def test_some_printing(self):
        print 'Test is running'

class TestFailure(TestCase):
    def test_failure(self):
        1/0

    def test_some_failure(self):
        raise Exception('Our information required for test analysis')

    def test_if_failrure(self):
        if 2*2 == 4:
            raise Exception('Validation failed')

    def test_if_passed(self):
        if 2 * 2 != 4:
            raise Exception('Validation should not failed')