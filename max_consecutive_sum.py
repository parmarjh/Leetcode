
def maxSubArray( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_sum = nums[0] 
    curr_sum = nums[0] 
    for i in nums[1:]:
        sum = curr_sum + i
        curr_sum = max(0,sum)
        max_sum = max(max_sum,curr_sum)
    return max_sum

data = list(map(int, input().split(',')))
print(maxSubArray(data))