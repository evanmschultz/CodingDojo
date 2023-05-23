/*  
    build for loop
    start at 0
    end at 6
    increment by 1
    if i is even and greater than 0, print "Here's your candy."
*/

/*
    We need a for loop because the runner's distance run changes sequentially,
    and the task of giving out candy will be repeated (a set number of times).
*/

// the for loop starts at 0 and ends at 6, incrementing by 1, and we only need 1 variable
for (var i = 0; i < 7; i++) {
    if (i % 2 == 0 && i != 0) {
        console.log("Here's your candy.");
    }
    else {
        console.log("Keep running, just one more mile and you get a piece of candy!")
    }
}

/* 
    Create a new loop where the runner only gets a piece of candy every 2 miles AND if they were going faster than 5.5 miles per hour.
*/

// set variable for runner's speed
var speed = 5.5;

// the for loop starts at 0 and ends at 6, incrementing by 1, and we only need 2 variables are needed (i and speed)

for (var i = 0; i < 7; i++) {
    // don't do anything unless the runner has gone at least 1 mile
    if (i > 0) {
        if (i % 2 == 0 && speed >= 5.5) {
            // if the runner is on an even mile and is going fast enough give them candy
            console.log("Here's your candy.");
        }
        else if (i % 2 != 0 && speed < 5.5) {
            // if the runner is on an even mile number but isn't going fast enough, don't give them candy but encourage them
            console.log("Speed up, you missed out on your piece of candy!")
        }
        else if (i % 2 != 0 && speed >= 5.5) {
            // if the runner is on an odd mile number and is going fast enough, encourage them
            console.log("You're doing great. 1 more mile and you get some candy!")
        }
        else {
            // if the runner is on an odd mile number and is not going fast enough, encourage them to speed up
            console.log("Speed up and keep going for another mile to get some candy!")
        }
    }
}

var x = 1

for (i = 0; i < 3; i += 2) {
    x += 1
}

console.log(x)
console.log(i)