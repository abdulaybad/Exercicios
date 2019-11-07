import math_fun
import pytest

def test_add():
	assert math_fun.add(7,3) == 10
	assert math_fun.add(7,1) == 8


def test_product():
	assert math_fun.product(5,5) == 25
	assert math_fun.product(5,3) == 15
	
def test_division():
	assert math_fun.division(2,-1) == -2
	assert math_fun.division(2,2) == 1


def test_listas():
	assert len(math_fun.listas()) == 9

def test_listas_erro():
	assert len(math_fun.listas()) != 5