/**
 * @param {string} s
 * @return {string}
 */
function reverseVowels(s) {
  let vowels = "aeiou";
  let vIndex = [];
  let vVowels = [];
  let result = s.split('');

  for (i = 0; i < s.length; i++) { 
    if(vowels.includes(s[i].toLowerCase())) {
      vIndex.push(i);
      vVowels.push(s[i]);
    }
  }

  let vChars = vVowels.reverse();
/*  
  console.log(`vChars: ${vChars}`);
  console.log(`vIndex: ${vIndex}`);
  console.log(`input: ${result}`);
*/  

  for (i = 0; i < vIndex.length; i++) {
      result[vIndex[i]] = vChars[i];
  }

//  console.log(`result: ${result.join('')}`);

  return result.join('');
};

let input = "IceCreAm";
console.log(reverseVowels(input)); // "AceCreIm"

input = "aA";
console.log(reverseVowels(input));
