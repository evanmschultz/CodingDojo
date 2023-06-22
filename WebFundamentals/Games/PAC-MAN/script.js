let world = [
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 1, 0, 2, 1, 2, 0, 1, 0, 0],
    [2, 2, 0, 2, 0, 0, 0, 2, 2, 2],
    [2, 2, 0, 0, 2, 2, 0, 2, 1, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 2, 0, 0, 0, 2, 2],
    [2, 2, 2, 2, 0, 1, 2, 0, 0, 2],
    [2, 1, 0, 0, 0, 0, 2, 0, 1, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
]

function displayWorld() {
    let output = ""

    for (i = 0; i < world.length; i++) {
        output += '<div class="row">\n' // create row opening tag

        for (j = 0; j < world[i].length; j++) {
            if (world[i][j] == 2) {
                output += '\t<div class="brick"></div>\n' // add brick div
            } else if (world[i][j] == 1) {
                output += '\t<div class="coin"></div>\n' // add coin div
            } else {
                output += '\t<div class="empty"></div>\n' // add empty div
            }
        }

        output += "</div>\n" // close row tag
    }
    // console.log(output)
    document.getElementById("world").innerHTML = output // pass output to document
}

displayWorld()

let pacManPosition = {
    x: 0,
    y: 4,
}
let coinCount = 0

function displayPacMan(x, y) {
    // named with let to make it clear it is being updated
    let pacMan = document.getElementById("pac-man")

    // update current position in position object
    pacManPosition.x = x
    pacManPosition.y = y

    // update the styling
    pacMan.style.top = `${pacManPosition.y * 26 + 3}px`
    pacMan.style.left = `${pacManPosition.x * 26 + 3}px`

    checkForCoin()
}

// set starting position
displayPacMan(pacManPosition.x, pacManPosition.y)

function checkForCoin() {
    const pacManX = pacManPosition.x
    const pacManY = pacManPosition.y

    if (world[pacManY][pacManX] == 1) {
        let coinCountDisplay = document.getElementById("coin-count")
        coinCount++

        coinCountDisplay.innerText = `Coin Count: ${coinCount}` // update count on screen

        world[pacManY][pacManX] = 0 // remove coin

        displayWorld() // refresh world
    }
}

document.onkeydown = function (event) {
    const key = event.key

    // get the integer value of the current position
    let pacManX = pacManPosition.x
    let pacManY = pacManPosition.y

    if (key == "ArrowRight" && world[pacManY][pacManX + 1] != 2) {
        // add one to check for collision or move right one, displayPacMan()
        pacManX++

        // check if leaving maze
        if (pacManX > world[0].length) {
            console.log("map complete")
            return
        }
    } else if (
        key == "ArrowLeft" &&
        world[pacManY][pacManX - 1] != 2 &&
        pacManX - 1 >= 0
    ) {
        // subtract one to check for collision move left one, displayPacMan()
        pacManX--

        // check if leaving maze
        if (pacManX < 0) {
            // if the move is left of the maze
            console.log("off map left")
        }
    } else if (key == "ArrowUp" && world[pacManY - 1][pacManX] != 2) {
        console.log("called")
        // subtract because it is distance from the top, move up
        pacManY--
    } else if (key == "ArrowDown" && world[pacManY + 1][pacManX] != 2) {
        // add because it is distance from the top, move down
        pacManY++
    }

    displayPacMan(pacManX, pacManY) // update display
}
