import numpy as np


def make_big_array():
    return np.zeros((1024, 1024, 50), dtype="uint8")


def make_two_arrays():
    arr1 = np.zeros((1024, 1024, 10))
    arr2 = np.ones((1024, 1024, 10))
    return arr1, arr2


def main():
    _arr1, _arr2 = make_two_arrays()
    _another_arr = make_big_array()


main()
