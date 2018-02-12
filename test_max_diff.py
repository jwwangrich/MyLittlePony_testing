def test_max_diff():
    from sum_num import MaxDiff
    maxdiff_output_1 = MaxDiff([-5, 2, 6, 1, -7, 10])
    maxdiff_output_2 = MaxDiff([9, 8, -7, 6, 5, -4])
    maxdiff_output_3 = MaxDiff([0.5, -0.9, 0.1, -0.2])
    assert maxdiff_output_1 == 17
    assert maxdiff_output_2 == 15
    assert maxdiff_output_3 - 1.4 < 0.0001
