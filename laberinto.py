def subsets(nums):
    def backtrack(first=0, curr=[]):
        output.append(curr)
        for i in range(first, n):
            backtrack(i + 1, curr + [nums[i]])

    output = []
    n = len(nums)
    backtrack()
    return output



