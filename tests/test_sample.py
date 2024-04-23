"""This File is used for Testing Purpose"""

import pytest


@pytest.fixture
def passing():
    """Dummy Fixture"""
    return True


def test_sample(passing):
    """
    Dummy test sample
    """
    assert passing
