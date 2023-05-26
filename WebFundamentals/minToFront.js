/*
create a function minToFront() such that the minimum value in the array is moved to index 0 while 
not changing the order of the rest of the array
*/

// find the minimum value
// store its minIndex number
// move all the values in indexes below minIndex up 1 and store the minimum value in index 0

function minToFront(arr) {
    let min = arr[0]
    let minIndex = 0

    // find min and minIndex
    for (i = 0; i < arr.length; i++) {
        if (arr[i] < min) {
            min = arr[i]
            minIndex = i
        }
    }

    // reassign all values to their new location starting at minIndex and decrementing
    for (i = minIndex; i > 0; i--) {
        arr[i] = arr[i - 1]
    }

    arr[0] = min

    return arr
}

// function that creates random arrays
function randArr() {
    let newArr = []
    // random array length up to 8
    let length = 0

    // ensure get a non 0 length value``
    while (length < 1) {
        length = Math.floor(Math.random() * 8)
    }
    console.log("The random array length is:", length)

    // populate newArr with random values up to 100
    for (i = 0; i < length; i++) {
        // get 0 or 1
        let isPos = Math.round(Math.random())

        // set multiplier sign to 1
        let sign = 1

        // change multiplier sign to -1 if isPos is 0
        if (isPos == 0) {
            sign = -1
        }

        // get random value
        let value = sign * Math.random() * 100

        newArr.push(value)
    }

    console.log("The random array is:", newArr)
    return newArr
}

let arrTest1 = [0, 10, 9, -1, 0]

console.log("The new array is:", minToFront(arrTest1))
console.log("The new array is:", minToFront(randArr()))
