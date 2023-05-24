// Debug the following code that removes negative values from an array

function removeNegatives(arr) {
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] <= 0) {
            // removes element at index i from arr
            arr.splice(i, 1)
        }
    }
    return arr
}

var result = removeNegatives([3, 7, -23, 0, 2.5, -4])
console.log(result)
