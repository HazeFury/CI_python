from operations.addition import add
from operations.substraction import substract
from operations.multiply import mult
from operations.divide import div


def test_addition_given_2_and_2_should_return_4():
    assert add(2, 2) == 4


def test_substraction_given_5_and_2_should_return_3():
    assert substract(5, 2) == 3


def test_multiply_given_2_and_10_should_return_3():
    assert mult(2, 10) == 20


def test_divide_given_15_and_3_should_return_3():
    assert div(15, 3) == 5
