def test_max_diff():
    from sum_num import MaxDiff
    import math
    import pytest
    maxdiff_output_1 = MaxDiff([-5, 2, 6, 1, -7, 10])
    maxdiff_output_2 = MaxDiff([9, 8, -7, 6, 5, -4])
    maxdiff_output_3 = MaxDiff([0.5, -0.9, 0.1, -0.2])
    maxdiff_output_4 = MaxDiff(['sdj', 5, 8, 10])
    assert maxdiff_output_1 == 17
    assert maxdiff_output_2 == 16
    assert maxdiff_output_3 - 1.4 < 0.0001
    with pytest.raises(ValueError):
        MaxDiff(math.sqrt(2), math.sqrt(-5), math.sqrt(8))
    with pytest.raises(TypeError):
        MaxDiff('9', 5, 9, 5, 9, 5)
    with pytest.raises(ImportError):
        import MyLittlePony_testing
