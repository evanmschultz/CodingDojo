/* 
Joe drives a taco truck in the booming town of Squaresburg. He uses an array of [x,y] coordinates corresponding to the 
locations of his customers. He also uses an array of [x,y] as coordinates corresponding to the location where he parks 
his truck. Customers walk from their location to his truck, but Joe wants to minimize the total distance from his truck 
to his customers, so he's looking for a better place to park. Feature request: given a customer coordinate array, return 
an optimal taco truck location.


Here's what we know: City blocks are perfect squares, and every street is two-way, at perfect right angles. He only parks 
by street corners (coordinates like [37,-16]). Customers only travel on streets: coordinate [2,-2] is distance 4 from 
[0,0]. Joe checks the array before deciding where to park. Given a customer coordinate array, return an optimal taco truck 
location.
*/

let customers = [
    [0, 0],
    [-2, 0],
    [1, 3],
    [-3, -3],
]
let customers2 = [
    [4, 4],
    [0, 0],
    [0, 0],
    [4, 4],
]

function truckLocation(arr) {
    // assign variable sum of x and y coordinates to calculate avg and set to 0
    let sumX = 0
    let sumY = 0

    // iterate through array to calculate sumX and sumY
    for (i = 0; i < arr.length; i++) {
        sumX += arr[i][0]
        sumY += arr[i][1]
    }

    // calculate avg's
    let avgX = Math.round(sumX / arr.length)
    let avgY = Math.round(sumY / arr.length)

    let response = `The optimal truck location is: ${[avgX, avgY]}`

    return response
}

console.log(truckLocation(customers))
console.log(truckLocation(customers2))
