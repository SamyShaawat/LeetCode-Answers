/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = (functions)=> {
    if (functions.length === 0 ){
        return function(x) {return x;}

    }
    return function(x) {
        let result = x;
        for (let i = functions.length - 1; i >= 0; i--) {
        result = functions[i](result);
        }
        return result;
  }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */