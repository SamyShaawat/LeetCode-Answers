/**
 * @param {string} s
 * @param {string} part
 * @return {string}
 */
var removeOccurrences = function(s, part) {
    let resultStack = [];
    let targetLength = part.length;
    let targetEndChar = part[part.length - 1];

    for (let currentChar of s) {
        resultStack.push(currentChar);

        if (currentChar === targetEndChar && resultStack.length >= targetLength) {
            if (resultStack.slice(-targetLength).join('') === part) {
                resultStack.length -= targetLength;
            }
        }
    }
    return resultStack.join('');
};