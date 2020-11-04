#Problem : https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3298/

def findMaxLength(nums):

        maxy =0 
        for i in range(len(nums)):
            for  j in range(i+1,len(nums)):
                if nums[i:j+1].count(0) == nums[i:j+1].count(1):
                    maxy = max(j-i+1, maxy)
        return maxy

print(findMaxLength(list(map(int,input().split(',')))))




# Approch : 2

# Algorithm

# In this approach, we make use of a countcount variable, which is used to store the relative number of ones and zeros encountered so far while traversing the array. The countcount variable is incremented by one for every \text{1}1 encountered and the same is decremented by one for every \text{0}0 encountered.

# We start traversing the array from the beginning. If at any moment, the countcount becomes zero, it implies that we've encountered equal number of zeros and ones from the beginning till the current index of the array(ii). Not only this, another point to be noted is that if we encounter the same countcount twice while traversing the array, it means that the number of zeros and ones are equal between the indices corresponding to the equal countcount values. The following figure illustrates the observation for the sequence [0 0 1 0 0 0 1 1]:

# Contiguous_Array

# In the above figure, the subarrays between (A,B), (B,C) and (A,C) (lying between indices corresponing to count = 2count=2) have equal number of zeros and ones.

# Another point to be noted is that the largest subarray is the one between the points (A, C). Thus, if we keep a track of the indices corresponding to the same countcount values that lie farthest apart, we can determine the size of the largest subarray with equal no. of zeros and ones easily.

# Now, the countcount values can range between \text{-n}-n to \text{+n}+n, with the extreme points corresponding to the complete array being filled with all 0's and all 1's respectively. Thus, we make use of an array arrarr(of size \text{2n+1}2n+1to keep a track of the various countcount's encountered so far. We make an entry containing the current element's index (ii) in the arrarr for a new countcount encountered everytime. Whenever, we come across the same countcount value later while traversing the array, we determine the length of the subarray lying between the indices corresponding to the same countcount values.

# JAVA Solution
public class Solution {

    public int findMaxLength(int[] nums) {
        int[] arr = new int[2 * nums.length + 1];
        Arrays.fill(arr, -2);
        arr[nums.length] = -1;
        int maxlen = 0, count = 0;
        for (int i = 0; i < nums.length; i + +) {
            count = count + (nums[i] == 0 ? -1 : 1);
            if (arr[count + nums.length] >= -1) {
                maxlen = Math.max(maxlen, i - arr[count + nums.length]);
            } else {
                arr[count + nums.length] = i;
            }

        }
        return maxlen;
    }
}