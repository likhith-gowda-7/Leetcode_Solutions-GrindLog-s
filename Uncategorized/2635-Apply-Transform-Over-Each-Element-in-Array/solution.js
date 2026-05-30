/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
let transformarr=[];
    for(let i=0;i<arr.length;i++){
   transformarr[i]=fn(arr[i],i);
}
        return transformarr;
};