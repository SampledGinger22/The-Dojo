/* 
  Given to me (Neil) in an interview
  Given a string
  return whether or not it's possible to make a palindrome out of the string's
  characters.
  What is it about a string that makes it possible for it to become a
  palindrome?
*/

const str1 = '';
const expected1 = false;

const str2 = 'a';
const expected2 = true;

const str3 = 'ddaa';
const expected3 = true;
// Explanation: "daad" or "adda"

const str4 = 'dda';
const expected4 = true;
// Explanation: "dad"

const str5 = 'aaadd';
const expected5 = true;
// Explanation: "daaad"

const str6 = 'abc';
const expected6 = false;

/**
 * Determines whether or not it is possible for the string's characters to be
 * rearranged into a palindrome.
 * - Space: O(?).
 * - Time: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given str can be rearranged into a palindrome.
 */
function canStringBecomePalindrome(str) {
    let countArr = [];
    if(str.length === 0){
        return false;
    }
    if(str.length === 1){
        return true;
    }

    for(let one in str){
        if(!countArr[str[one]]){
            countArr[str[one]] = 1;
        }
        else if(countArr[str[one]]){
            countArr[str[one]] += 1;
        }
    }
    
    let hasOdd = false;

    for(let key in countArr){
        if(countArr[key] % 2 === 1 && hasOdd === false){
            hasOdd = true;
        }
        else if(countArr[key] % 2 === 1 && hasOdd === true){
            return false;
        }
    }

    return true;
}

console.log(canStringBecomePalindrome(str1));