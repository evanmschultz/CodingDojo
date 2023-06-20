function pizzaOven(crust, sauceType, cheese, toppings) {
    var pizza = {}

    pizza.crust = crust
    pizza.sauceType = sauceType
    pizza.cheese = cheese
    pizza.toppings = toppings

    return pizza
}

// options for random pizza generator
let crustOptions = ["thin", "regular", "deep dish"]
let sauceOptions = ["traditional", "ranch", "pesto"]
let cheeseOptions = ["mozzarella", "feta", "cheddar"]
let toppingOptions = [
    "olives",
    "onions",
    "pepperoni",
    "prosciutto",
    "peppers",
    "mushrooms",
]

function randomPizza() {
    // random numbers for the amount of options to pick
    var numOfCheeses = Math.floor(
        Math.random() * (cheeseOptions.length - 1) + 1 // ensure there is at least one cheese selection
    )
    var numOfToppings = Math.floor(Math.random() * toppingOptions.length)

    var crust = crustOptions[Math.floor(Math.random() * crustOptions.length)]
    var sauce = sauceOptions[Math.floor(Math.random() * sauceOptions.length)]
    var cheeses = []
    var toppings = []

    // loop to get all cheese choices
    for (i = 0; i < numOfCheeses; i++) {
        var cIndex = Math.floor(Math.random() * cheeseOptions.length)
        cheeses.push(cheeseOptions[cIndex])
    }

    // loop to get all topping choices
    for (j = 0; j < numOfToppings; j++) {
        var tIndex = Math.floor(Math.random() * toppingOptions.length)
        toppings.push(toppingOptions[tIndex])
    }

    return pizzaOven(crust, sauce, cheeses, toppings)
}

console.log(
    pizzaOven(
        "deep dish",
        "traditional",
        ["mozzarella"],
        ["pepperoni", "sausage"]
    )
)
console.log(
    pizzaOven("thin", "ranch", ["mozzarella"], ["extra cheese", "basil"])
)
console.log(
    pizzaOven(
        "traditional",
        "regular",
        ["mozzarella", "feta"],
        ["olives", "mushrooms", "peppers"]
    )
)

console.log("\nrandom pizza:\n", randomPizza())
