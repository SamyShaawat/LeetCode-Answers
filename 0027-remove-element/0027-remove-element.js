/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    while (nums.includes(val)) {
        index = nums.indexOf(val)
        nums.splice(index, 1);
    }
    k =  nums.length
    return k;
};