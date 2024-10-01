import pytest
import Closest

def testClosest1():
    expected = (-13, -14)
    actual = Closest.closest_pair([-13, 5, 18, 7, -14, 21])
    assert actual == expected
