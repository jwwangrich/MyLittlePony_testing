from sum_num import sum_numbers, MaxDiff, findextremes


class MyList():

    def __init__(self, list = None):
        self.list = list

    def MaxDiff(self):
        self.Max_diff_result = MaxDiff(self.list)
        return self.Max_diff_result

    def sum_numbers(self):
        self.sum_results = sum_numbers(self.list)
        return self.sum_results

    def findextremes(self):
        self.extreme_result = findextremes(self.list)
        return self.extreme_result
