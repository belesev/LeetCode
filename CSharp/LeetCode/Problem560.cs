/// <summary>
/// https://leetcode.com/problems/subarray-sum-equals-k/
/// 
/// Given an array of integers nums and an integer k, return the total number of continuous subarrays whose 
/// sum equals to k.
/// </summary>

namespace Problem560
{
    public class Solution
    {
        public int SubarraySum(int[] nums, int k)
        {
            var result = 0;

            var sumFromBeginning = new int[nums.Length + 1];
            sumFromBeginning[0] = 0;
            for (var i = 1; i < nums.Length + 1; i++)
                sumFromBeginning[i] = sumFromBeginning[i - 1] + nums[i - 1];

            for (var i = 0; i < sumFromBeginning.Length; i++)
            for (var j = i + 1; j < sumFromBeginning.Length; j++)
                if (sumFromBeginning[j] - sumFromBeginning[i] == k)
                    result++;

            return result;
        }
    }
}