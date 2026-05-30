/**
 * @param {number[]} arr
 * @return {number[]}
 */
var arrayRankTransform = function(arr) {
    if(arr.length==0)return [];
let sort_arr = [...new Set(arr)].sort((a, b) => a - b);
let rank={};
for(let i=0;i<arr.length;i++){
   rank[sort_arr[i]]=i+1;
}
return arr.map(val=>rank[val])
};