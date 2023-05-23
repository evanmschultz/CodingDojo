function greeting(name, time) {
    if (name == "Fry") {
        console.log("Hello, Fry. Good", time + "!")
    }
    else {
        console.log("Go away", name + ".", "Its ", time + "!")
    }
}

greeting("Lela", "afternoon")
greeting("Fry", "morning")

// I didn't fully read the checklist. I thought it was more open ended. 

function greet(name, time) {
    if (name == "Anakin") {
        console.log("Good", time + ",", "Anakin!")
    }
    else if (name == "Count Dooku") {
        console.log("I'm coming for you, Dooku. It's", time + "!")
    }
    else {
        console.log("It's a nice", time, "isn't it", name)
    }
}

greet("Anakin", "evening")
greet("Count Dooku", "morning")
greet("Padme", "night")