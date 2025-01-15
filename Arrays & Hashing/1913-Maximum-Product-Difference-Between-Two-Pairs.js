/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProductDifference = function(nums) {
    let sorted = nums.sort((a,b) => a- b)
    let maxProduct =  (nums[nums.length - 1] * nums[nums.length - 2]) - (nums[0] * nums[1]);
    console.log(maxProduct)
    return maxProduct
};