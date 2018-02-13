def test_minmax():
    from minmax import findextremes
    FindExtremes_Output1 = findextremes([0, -1.5, -2, -7, -53])
    FindExtremes_Output2 = findextremes([0, 3.2, 2, 10, 6])
    FindExtremes_Output3 = findextremes([2, -3, 54, 6, 10])
    assert FindExtremes_Output1 == (-53,0)
    assert FindExtremes_Output2 == (0,10)
    assert FindExtremes_Output3 == (-3,54)

