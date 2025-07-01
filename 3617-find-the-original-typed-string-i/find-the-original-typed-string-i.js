/**
 * @param {string} word
 * @return {number}
 */
var possibleStringCount = function(word) {
    let n=word.length;
    let count=n;
    
    for(let i=1;i<n;i++){
        if(word[i]!==word[i-1]){
            count--;
        }
    }
    return count;
};