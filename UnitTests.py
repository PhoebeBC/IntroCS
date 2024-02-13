import requests
import pytest


def multiply(a: float, b: float):
    return a * b


def reverse_list(normal_list: list):
    return normal_list.reverse()


def get_webpage_date(url):
    website = requests.get(url)
    return website.headers["Date"]


def test_multiply():
    assert multiply(2,2) == 4


def test_multiply_negative():
    assert multiply(2, -2) == -4


def test_multiply_decimal():
    assert multiply(2.5,2.5) == 5.25