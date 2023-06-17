/* 
    1) Write a function that is given an array and each time the value is 
    "food" it should console log "yummy". If "food" was not present in the 
    array console log "I'm hungry" once.
*/
console.log("challenge 1\n")
function alwaysHungry(array) {
    let hasFood = false

    for (value of array) {
        if (value == "food") {
            console.log("yummy", "yummy")

            hasFood = true
        }
    }

    if (!hasFood) {
        console.log("I'm hungry")
    }
}

alwaysHungry([3.14, "food", "pie", true, "food"])
// this should console log "yummy", "yummy"
alwaysHungry([4, 1, 5, 7, 2])
// this should console log "I'm hungry"

/* 
    2) Given an array and a value cutoff, return a new array containing only 
    the values larger than cutoff. 
*/
console.log("\nchallenge 2\n")
function highPassFilter(array, minimum) {
    let tempArray = []

    for (num of array) {
        if (num > minimum) {
            tempArray.push(num)
        }
    }

    return tempArray
}

let hungryResult = highPassFilter([6, 8, 3, 10, -2, 5, 9], 5)
console.log(
    `the elements that were higher than the minimum are [${hungryResult}]`
) // expect back [6, 8, 10, 9]

/*  
    3) Given an array of numbers return a count of how many of the numbers are larger than the average.
*/
console.log("\nchallenge 3\n")
function betterThanAverage(array) {
    let sum = 0

    for (num of array) {
        sum += num
    }

    let average = sum / array.length
    let aboveAverage = 0

    for (num of array) {
        if (num > average) {
            aboveAverage += 1
        }
    }

    return aboveAverage
}

let averageResult = betterThanAverage([6, 8, 3, 10, -2, 5, 9])
console.log(`there are ${averageResult} numbers above the average`) // expect back 4

/* 4) Write a function that will reverse the values an array and return them. */
console.log("\nchallenge 4\n")
function reverseArray(array) {
    // use pointers: python a, b = b, a // JS doesn't have that without using an array, use temp variable
    let left = 0
    let right = array.length - 1

    while (left < right) {
        let tempValue = array[left]

        array[left] = array[right]
        array[right] = tempValue

        left++
        right--
    }

    return array
}

let reverseResult = reverseArray(["a", "b", "c", "d", "e"])
console.log(`the reversed array is [${reverseResult}]`) // expect back ["e", "d", "c", "b", "a"]

/* 5) Fibonacci numbers have been studied for years and appear often in nature. Write a function 
that will return an array of Fibonacci numbers up to a given length n. Fibonacci numbers are calculated 
by adding the last two values in the sequence together. So if the 4th value is 2 and the 5th value is 3 
then the next value in the sequence is 5. */
console.log("\nchallenge 5\n")
function fibonacciArray(length) {
    let outputArray = [0, 1]
    let num = 0

    if (length < 1) {
        return []
    }
    if (length == 1) {
        return outputArray
    }

    for (i = 1; i < length - 1; i++) {
        num = outputArray[i] + outputArray[i - 1]

        outputArray.push(num)
    }

    return outputArray
}
let inputNum = 10
let fibonacciResult = fibonacciArray(inputNum)
console.log(
    `the fibonacci sequence with ${inputNum} equals [${fibonacciResult}]`
)
