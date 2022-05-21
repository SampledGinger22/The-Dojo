/* 
  Array: Mode
  
  Create a function that, given an array of ints,
  returns the int that occurs most frequently in the array.
  What if there are multiple items that occur the same number of time?
    - return all of them (in an array)
    - what if all items occur the same number of times?
      - return empty array
*/

const nums1 = [];
const expected1 = [];

const nums2 = [1];
const expected2 = [1];

const nums3 = [5, 1, 4];
const expected3 = [];

const nums4 = [5, 1, 4, 1];
const expected4 = [1];

const nums5 = [5, 1, 4, 1, 5];
const expected5 = [5, 1];

const nums6 = [5, 4, 1, 4, 1, 5];
const expected6 = [];
//  - order doesn't matter

/**
 * Finds the mode or all modes if there are more than one. The mode is the
 *    value which occurs the most times in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums Test
 * @returns {Array<number>} Mode or modes in any order.
 */
function mode(nums) {
    var obj_1 = {};
    var greatest_val = [];
    for(var i = 0; i < nums.length; i++){
        if(obj_1[nums[i]] === undefined){
            obj_1[nums[i]] = 1;
        }
        else if(obj_1[nums[i]] !== undefined){
            obj_1[nums[i]] += 1;
        }
    }
    console.log(Object.keys(obj_1[0])
    greatest_val.push(obj_1[0]);
    console.log(greatest_val)
    for(var j = 1; j < obj_1.length; i++){
        if (obj_1[j] > obj_1[greatest_val[0]]){
            greatest_val = [];
            greatest_val.push(obj_1[j]);
            
        }
        // else if(obj_1[j] === obj_1[greatest_val[0]]){
        //     greatest_val.push[obj_1[j]];
        // }
    }
    return(greatest_val)
}
console.log(mode(nums4))