/**
 * @param {number[]} arr
 * @param {number} k
 * @param {number} threshold
 * @return {number}
 */



var numOfSubarrays = function(arr, k, threshold) {
    let maxSub = 0
    let start = 0
    let currAvg = 0

    for (let end = 0; end < arr.length; end++){
        currAvg += arr[end]

        while (end - start +1 >= k){
            console.log('before', currAvg)
            let calculatedAvg = currAvg / k
            console.log('after', calculatedAvg)

            if (calculatedAvg >= threshold){
                maxSub += 1
            }
            currAvg -= arr[start]
            start += 1
        }
    }
    console.log(maxSub)
    return maxSub
};
