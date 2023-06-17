/* 
    1) Write a function that is given an array and each time the value is 
    "food" it should console log "yummy". If "food" was not present in the 
    array console log "I'm hungry" once.
*/
console.log("challeng 1\n")
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
console.log("\nchalleng 2\n")
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
console.log("\nchalleng 3\n")
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
