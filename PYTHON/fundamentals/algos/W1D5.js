/* 
  Zip Arrays into Map
  
  
  Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.
  Associative arrays are sometimes called maps because a key (string) maps to a value 
 */

  const keys1 = ["abc", 3, "yo"];
  const vals1 = [42, "wassup", true];
  const expected1 = {
    abc: 42,
    3: "wassup",
    yo: true,
  };

  const keys3 = ["abc", 3, "yo", "something"];
  const vals3 = [42, "wassup", true];
  const expected3 = {
    abc: 42,
    3: "wassup",
    yo: true,
    something: ''
  };

  const keys4 = ["abc", 3, "yo"];
  const vals4 = [42, "wassup", true, "something"];
  const expected4 = false
  
  const keys2 = [];
  const vals2 = [];
  const expected2 = {};
  
  /**
   * Converts the given arrays of keys and values into an object.
   * - Time: O(?).
   * - Space: O(?).
   * @param {Array<string>} keys
   * @param {Array<any>} values
   * @returns {Object} The object with the given keys and values.
   */



// function zipArraysIntoMap(keys, values) {
//     var temp = {};
//     for(var i = 0; i < keys.length; i++){
//         temp[keys[i]] = values[i];
//     }
//     console.log(temp);
// }

// zipArraysIntoMap(keys3, vals3)





//////////////////////////////////////////////////////////////////////////////////////////////


  /* 
  Invert Hash
  A hash table / hash map is an obj / dictionary
  Given an object / dict,
  return a new object / dict that has the keys and the values swapped so that the keys become the values and the values become the keys
*/

const two_obj1 = { name: "Zaphod", charm: "high", morals: "dicey" };
const two_expected1 = { Zaphod: "name", high: "charm", dicey: "morals" };

// bonus
const two_obj2 = { name: "Zaphod", charm: "high", morals: "dicey", something:["thing1", "thing2"] };
const two_expected2 = { Zaphod: "name", high: "charm", dicey: "morals", thing1:"something", thing2:"something"  };

const two_obj3 = { name: "Zaphod", charm: "high", morals: "dicey", something:"dicey"  };
const two_expected3 = { Zaphod: "name", high: "charm", dicey: ["morals", "something"]  };

/**
 * Inverts the given object's key value pairs so that the original values
 * become the keys and the original keys become the values.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Object<string, any>} obj
 * @return The given object with key value pairs inverted.
 */
// function invertObj(obj) {
//     newObj = {};
//     for (var key in obj){
//         if(obj[key][1].length < 0) {
//             for(var i = 0 ; i < obj[key].length; i++){
//                 newObj[obj[key][i]]=key;
//             }
//         }
//         newObj[obj[key]] = key;
//     }
//     return newObj;
// }
// console.log(invertObj(two_obj2));
//   }