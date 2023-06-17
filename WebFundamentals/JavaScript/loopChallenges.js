/* 1) print all odd numbers from 1-20 */
function oddNums(range) {
    console.log(`oddNums called with range: ${range}\n`)
    for (i = 1; i <= range; i++) {
        if (i % 2 != 0) {
            console.log(i)
        }
    }
    console.log("\n")
}

oddNums(20)

/* 2) print all factors of 3 from 100-0 */
function multiplesOf3(startingNum) {
    console.log(`multiplesOf3 called with starting number: ${startingNum}\n`)
    let num = startingNum

    while (num > 0) {
        if (num % 3 == 0) {
            console.log(num)
        }
        num--
    }
    console.log("\n")
}

multiplesOf3(100)

/* 3) print the values in the sequence [4, 2.5, 1, -0.5, -2, -3.5] */
function printSequence(array) {
    console.log(`printSequence called`)
    console.log("with for in\n")
    for (i in array) {
        // `for in` loops over iterable by key
        console.log(array[i])
    }
    console.log("\nwith `for of`\n")
    for (num of array) {
        // `for of` loops over iterable by value
        console.log(num)
    }

    console.log("\nprintSequence end\n")
}

printSequence([4, 2.5, 1, -0.5, -2, -3.5])

/* 4) sum all the numbers from 1 to 100 */
function sigma(range) {
    console.log(`sigma called with range: range\n`)
    let sum = 0

    // using Gauss's summation method
    if (range % 2 == 0) {
        sum = (range + 1) * (range / 2)
    } else {
        sum = (range * (range + 1)) / 2
    }
    console.log(`the sum found with Gauss's = ${sum}\n`)

    // the way the challenge asked for
    sum = 0
    for (i = 1; i <= range; i++) {
        sum += i
    }
    console.log(`the sum using brute force = ${sum}\n`)

    return sum
}

sigma(100)

/* 5) find the factorial of 12 */
function factorial(number) {
    console.log("factorial called\n")
    if (number == 0) {
        return `${number} factorial = 1`
    } else if (number < 0) {
        return "cannot find the factorial of negative numbers"
    }

    let product = 1

    for (i = 0; i < number; i++) {
        product *= i + 1
    }

    return `${number} factorial = ${product}`
}

// uses recursion to find the factorial
function factorialRecursive(num) {
    if (num === 0 || num === 1) {
        return 1
    } else if (num < 0) {
        return NaN
    } else {
        return num * factorialRecursive(num - 1)
    }
}

let factorialInput = 12
console.log(factorial(factorialInput))
console.log(
    `The factorial of ${factorialInput} = ${factorialRecursive(factorialInput)}`
)
