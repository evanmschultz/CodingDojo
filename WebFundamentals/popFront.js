/* 
Given an array, remove and return the value at the beginning of the array. 
Do this without using any built-in array methods except pop().
*/

// store arr[0] as variable to be returned
// for loop to decrease index values > 0 by 1

function popFront(arr) {
    let front = arr[0]

    for (i = 0; i < arr.length - 1; i++) {
        arr[i] = arr[i + 1]
    }
    arr.pop()

    return front
}

// function that creates random arrays
function randArr() {
    let newArr = []
    let length = 0

    // ensure get a non 0 length value
    while (length < 1) {
        length = Math.floor(Math.random() * 10)
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
        let value = Math.round(sign * Math.random() * 100)

        newArr.push(value)
    }

    console.log("The random array is:", newArr)
    return newArr
}

array = randArr()
console.log("The first value of the array was:", popFront(array))
console.log("The updated array is:", array)
