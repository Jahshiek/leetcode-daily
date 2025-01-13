/**
 * @param {string[]} strs
 * @return {string}
 */








var longestCommonPrefix = function(strs) {
    let newStr = ''
    let commonPrefix = strs[0]

    for (let i = 0; i < commonPrefix.length; i++){
        let char =commonPrefix[i]
       for (let j = 1; j < strs.length; j++){
            if(char !== strs[j][i]) return newStr
        } 
        newStr += char
    }
    return newStr
}


