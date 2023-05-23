// #1
var arr1 = [8, 6, 7, 5, 3, 0, 9];
// #2
var arr2 = [4, 7, 13, 13, 19, 37, -2];
// #3
var arr3 = [6, 2, 12, 14, -24, 5, 0];


// 1. Write a for loop that will traverse through an array of numbers, and print each number.

function one(arr) {
    // take array and print each value

    for (i = 0; i < arr.length; i++) {
        console.log(arr[i])
    }
}

// test function one() with above arrays
// console.log("Test 1")
// testOne1 = one(arr1)
// testOne2 = one(arr2)
// testOne3 = one(arr3)

// 2. Write a for loop that will traverse through an array of numbers, and print the sum of the number and the index of the number in the array.

function two(arr) {
    // take any array and print the indexes of the each number in the array and its current sum, then return the total sum

    sum = 0

    for (i = 0; i < arr.length; i++) {
        sum += arr[i]
        console.log("At index", i, "the sum is", sum)
    }

    return sum
}

// test function two() with above arrays
// console.log("Test 2")
// testTwo1 = two(arr1)
// testTwo2 = two(arr2)
// testTwo3 = two(arr3)

// 3. Write a for loop that will traverse through an array of numbers, and print only the numbers greater than 5.

function three(arr) {
    // loop through array and print only the numbers greater than 5

    for (i = 0; i < arr.length; i++) {
        if (arr[i] > 5) {
            console.log(arr[i])
        }
    }
}

// test function three() with above arrays
// console.log("Test 3")
// testThree1 = three(arr1)
// testThree2 = three(arr2)
// testThree3 = three(arr3)

/*
    Ninja Bonus: Modify your solution for #3 so that any numbers in the array that are not greater than 5 are 
    instead replaced with a string of "No dice." This string should not be printed.
*/

function four(arr) {
    // loop through array and print only the numbers greater than 5

    for (i = 0; i < arr.length; i++) {
        if (arr[i] > 5) {
            console.log(arr[i])
        }
        else {
            arr[i] = "No dice."
        }
    }
}

// test function four() with above arrays
// console.log("Test 4")
// testFour1 = four(arr1)
// testFour2 = four(arr2)
// testFour3 = four(arr3)

// console.log(arr1)
// console.log(arr2)
// console.log(arr3)

function maxMinAvg(arr) {
    // set the variables needed
    // run for loop
    // push to new arr
    // return new array

    max = arr[0]
    min = arr[0]
    sum = 0
    arrnew = []

    for (var i = 0; i < arr.length; i++) {
        if (arr[i] > max) {
            max = arr[i]
        }
        if (arr[i] < min) {
            min = arr[i]
        }

        sum += arr[i]
    }

    avg = sum / arr.length
    arrnew.push(max)
    arrnew.push(min)
    arrnew.push(avg)

    return arrnew
}

// console.log("Arr test")
// console.log(maxMinAvg(arr1))

function swap(arr) {
    var arrnew = arr
    var temp1 = arr[0]
    var temp2 = arr[arr.length-1]

    arrnew[0] = temp2
    arrnew[arr.length-1] = temp1

    return arrnew
}

console.log(swap(arr1))
