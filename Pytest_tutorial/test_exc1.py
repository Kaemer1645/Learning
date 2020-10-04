from .exc1 import triangle_area
import pytest


def test_triangle_area(capsys):  #capsys - capture system -
    #given
    base = 10
    height = 8


    #when
    triangle_area(base, height)
    out, err = capsys.readouterr()

    #then
    assert out == '40.0\n'

