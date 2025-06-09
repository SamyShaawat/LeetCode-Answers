/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = (arr, fn)=> {
    let res = []
    for (let i = 0; i < arr.length; i++){
            if (fn(arr[i], i)){
                res.push(arr[i]);
            }else{
                continue;
            }
    }
    return res
};