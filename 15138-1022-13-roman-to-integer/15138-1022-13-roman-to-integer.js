/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    let dict1 = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    };
    let lst = [];
    for (let i = 0; i < s.length; i++) {
        lst.push(dict1[s[i]]);
    }
    let n = lst.length
    let result = 0;
    for (let i = 0; i < n - 1; i++) {
        if (lst[i] < lst[i + 1]) {
            result -= lst[i];
        } else {
            result += lst[i];
        }
    }
    result += lst[n - 1];
    return result;
};