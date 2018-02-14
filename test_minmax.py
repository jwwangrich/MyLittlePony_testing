def test_minmax():
    from sum_num import find_extremes
    FindExtremesOutput1 = find_extremes([0, -1.5, -2, -7, -53])
    FindExtremesOutput2 = find_extremes([0, 3.2, 2, 10, 6])
    FindExtremesOutput3 = find_extremes([2, -3, 54, 6, 10])
    assert FindExtremesOutput1 == (-53, 0)
    assert FindExtremesOutput2 == (0, 10)
    assert FindExtremesOutput3 == (-3, 54)
