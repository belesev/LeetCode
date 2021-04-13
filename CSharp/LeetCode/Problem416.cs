using System.Linq;

namespace Problem416
{
    public class Solution
    {
        public bool CanPartition(int[] nums)
        {
            var sum = nums.Sum();
            if (sum % 2 == 1)
                return false;

            return CanPartition(nums, 0, sum / 2);
        }

        private bool CanPartition(int[] nums, int startPtr, int rest)
        {
            if (rest == 0)
                return true;

            if (startPtr == nums.Length)
                return false;

            bool withFirstExcluded = CanPartition(nums, startPtr + 1, rest);
            if (withFirstExcluded)
                return true;

            bool withFirstIncluded = CanPartition(nums, startPtr + 1, rest - nums[startPtr]);
            if (withFirstIncluded)
                return true;

            return false;
        }
    }
}
