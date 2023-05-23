// create a function with two input parameters to calculate how many pieces of cake are leftover from an office party

function howMuchLeftOverCake(numberOfPieces, numberOfPeople) {
    var modulo =  numberOfPieces % numberOfPeople // calculates remainder based 
    
    if (numberOfPieces / numberOfPeople >= 2) { 
        // checks if there is enough left overs for each person to have another piece
        return "Hold another party!"
    }
    else if (modulo == 0) {
        // since there isn't enough for another party, and the remainder is 0, that means you had the exact correct amount of cake
        return "No leftovers for you!"
    }
    else if (modulo <= 2) {
        // checks if you personally have leftovers
        return "You have some leftovers"
    }
    else {
        // someone else can share in the leftovers with you, because you don't want to get that fat!
        return "You have leftovers to share"
    }
}

console.log(howMuchLeftOverCake(10,5))

function max(arr) {
    var max = arr[0]
    console.log(max)

    for (i=0; i<arr.length; i++) {
        if (arr[i] > max) {
            max = arr[i]
        }
    }

    return max
}

console.log(max([1,2,3,4]))

function avg(arr) {
    var sum = 0
    for (var i = 0; i < arr.length; i++){
        sum += arr[i]
    }
    return sum / arr.length
}

console.log(avg([1,2,3,4]))