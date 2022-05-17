/* 
  Given two arrays, interleave them into one new array.
  The arrays may be different lengths. The extra items should be added to the
  back of the new array.
*/

const arrA1 = [1, 2, 3];
const arrB1 = ["a", "b", "c"];
const expected1 = [1, "a", 2, "b", 3, "c"];

const arrA2 = [1, 3];
const arrB2 = [2, 4, 6, 8];
const expected2 = [1, 2, 3, 4, 6, 8];

const arrA5 = [1, 3, [1, 3, 5]];
const arrB5 = [2, 4, 6, 8];
const expected5 = [1, 2, 3, 4, [1, 3, 5], 6, 8];

const arrA3 = [1, 3, 5, 7];
const arrB3 = [2, 4];
const expected3 = [1, 2, 3, 4, 5, 7];

const arrA4 = [];
const arrB4 = [42, 0, 6];
const expected4 = [42, 0, 6];

/**
 * Interleaves two arrays into a new array. Interleaving means alternating
 * the items starting from the first array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<any>} arr1
 * @param {Array<any>} arr2
 * @returns {Array<any>} A new array of interleaved items.
 */


function interleaveArrays(arr1, arr2) {
    if (arr1.length === 0) return arr2
    if (arr2.length === 0) return arr1
    var arr3 = [];
    var i = 0;
    var j = 0;
    while(i < arr1.length && j < arr2.length){
        arr3.push(arr1[i]);
        i++;
        arr3.push(arr2[j]);
        j++;
    }
    if(i >= arr1.length) {
        while(j < arr2.length){
            arr3.push(arr2[j]);
            j++;
        }
    }
    else if (j >= arr2.length) {
        while (i < arr1.length){
            arr3.push(arr1[i]);
            i++;
        }
    }
    return arr3
}
console.log(interleaveArrays(arrA1, arrB1))
console.log(interleaveArrays(arrA2, arrB2))
console.log(interleaveArrays(arrA3, arrB3))
console.log(interleaveArrays(arrA4, arrB4))
console.log(interleaveArrays(arrA5, arrB5))


///////////////////////////////////////////////////////////////////////////////////////////


/* 
  Array: Binary Search (non recursive)
  Given a sorted array and a value, return whether the array contains that value.
  Do not sequentially iterate the array. Instead, ‘divide and conquer’,
  taking advantage of the fact that the array is sorted .
  Bonus (alumni interview): 
    first complete it without the bonus, because they ask for additions
    after the initial algo is complete
    return how many times the given number occurs
*/

const two_nums1 = [1, 3, 5, 6];
const two_searchNum1 = 4;
const two_expected1 = false;

const two_nums2 = [4, 5, 6, 8, 12];
const two_searchNum2 = 5;
const two_expected2 = true;

const two_nums3 = [3, 4, 6, 8, 12];
const two_searchNum3 = 3;
const two_expected3 = true;

// bonus, how many times does the search num appear?
const two_nums4 = [2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9];
const two_searchNum4 = 2;
const two_expected4 = 4;

/**
 * Efficiently determines if the given num exists in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} sortedNums
 * @param {number} searchNum
 * @returns {boolean} Whether the given num exists in the given array.
 */
function binarySearch(sortedNums, searchNum) {
    var startindex = 0;
    var endindex = sortedNums.length-1;
    var midindex = Math.floor((startindex + endindex) / 2);
    while(startindex < endindex){
        if(startindex == sortedNums[midindex]){
            return true;
        }
        else if(searchNum > sortedNums[midindex]){
            startindex = midindex;
            midindex = Math.floor((startindex + endindex) / 2);
        }
        else if (searchNum < sortedNums[midindex]){
            endindex = midindex;
            midindex = Math.floor((startindex + endindex)/2)
        }
    }
    return false
}
console.log(binarySearch(two_nums3, two_searchNum3))