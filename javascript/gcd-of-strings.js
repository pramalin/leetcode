
/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
function gcdOfStrings(str1, str2) {
    function isGcd(str, subStr) {
        if (str.length % subStr.length !== 0) {
            return false;
        }
    
        let repeatCount = str.length / subStr.length;
        return (str.split(subStr).length - 1 === repeatCount);
    }
    
    function findGcd(str) {
        let gcd = "";
        for (i = 0; i <= str.length / 2; i++) {
            let subStr = str.slice(0, i + 1);           
            if (isGcd(str, subStr)) {
                gcd = subStr;
                break;
            }
        }
        return gcd;
    }

    let gcd = "";
    let gcd1 = findGcd(str1);
    let gcd2 = findGcd(str2);
    console.log(`gcd1: ${gcd1} gcd2: ${gcd2}`);
    if(gcd1 === gcd2) {
      gcd = gcd1;
    } else if (gcd1 === str2) {
        gcd = gcd1;
    } else if (gcd2 === str1) {
        gcd = gcd2;
    }
    return gcd;
}


//console.log('isGcd("AAAAAB, "AB") "' + isRepeat("AAAAAB", "AB")); // true

var str1 = "ABCABC";
var str2 = "ABC";
console.log(`gcdOfStrings(${str1}, ${str2}) `);
console.log(gcdOfStrings(str1, str2)); // Output: "ABC"

str1 = "ABABAB";
str2 = "ABAB";
console.log(`gcdOfStrings(${str1}, ${str2}) `);
console.log(gcdOfStrings(str1, str2)); // Output: "ABC"

str1 = "LEET";
str2 = "CODE";
console.log(`gcdOfStrings(${str1}, ${str2}) `);
console.log(gcdOfStrings(str1, str2)); // Output: "ABC"

str1 = "AAAAAB";
str2 = "AAA";
console.log(`gcdOfStrings(${str1}, ${str2}) `);
console.log(gcdOfStrings(str1, str2)); // Output: "ABC"

str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX";
str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX";
console.log(`gcdOfStrings(${str1}, ${str2}) `);
console.log(gcdOfStrings(str1, str2)); // Output: "ABC"
