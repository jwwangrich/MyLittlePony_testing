from MyList import MyList
import pytest
import math

def test_sum_num():
    listA = MyList()
    assert(listA.sum_numbers() == 0)
    listA.sum_numbers(1)
    assert(listA.sum_numbers() == 1)
    listA.sum_numbers(5)
    assert (listA.sum_numbers() == 6)

def test_maxdiff():
    listB = MyList()
    assert(listB.MaxDiff() == 0)
    listB.MaxDiff(5)
    assert(listB.MaxDiff() == 5)
    listB.MaxDiff(8)
    assert(listB.MaxDiff() == 5)

def test_minmax():
    listC = MyList()
    assert(listC.findextremes() == 0)
    listC.findextremes(3)
    assert(listC.findextremes() == [0, 3])
    listC.findextremes(-1)
    assert(listC.findextremes() == [-1, 3])
