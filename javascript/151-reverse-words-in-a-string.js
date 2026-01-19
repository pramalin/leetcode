/**
 * @param {string} s
 * @return {string}
 */

function reverseWords(s) {
    let words = s.trim().split(/\s+/);
    let reversedWords = words.reverse();
    return reversedWords.join(' ');    
};
