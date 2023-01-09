/**
 *  https://leetcode.com/problems/two-sum/
 */
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int index1;
        int index2;
        int[] result1 = new int[2];

        for(int i = 0; i < nums.length; i++){
            for(int j = i+1; j < nums.length; j++){
                if(nums[i]+nums[j] == target){
                    index1 = i;
                    index2 = j;
                    result1[0] = index1;
                    result1[1] = index2;
                    return result1;
                }
            }// 2nd for end
        }// 1st for end

        return result1;
    }
}