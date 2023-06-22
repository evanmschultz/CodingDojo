let world = [
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 1, 0, 2, 1, 2, 0, 1, 0, 0],
    [2, 2, 0, 2, 0, 0, 0, 2, 2, 2],
    [2, 2, 0, 0, 2, 2, 0, 2, 1, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 2, 2, 2, 2, 1, 2, 0, 2, 2],
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
    x: 3,
    y: 3,
}

// set starting position
displayPacMan(pacManPosition.x, pacManPosition.y)

function displayPacMan(x, y) {
    // named with let to make it clear it is being updated
    let pacMan = document.getElementById("pac-man")

    // update current position in position object
    pacManPosition.x = x
    pacManPosition.y = y

    // update the styling
    pacMan.style.top = `${pacManPosition.y}px`
    pacMan.style.left = `${pacManPosition.x}px`
}

document.onkeydown = function (event) {
    const key = event.key

    // get the integer value of the current position
    let pacManTop = pacManPosition.y
    let pacManLeft = pacManPosition.x

    if (key == "ArrowRight") {
        pacManLeft += 26 // move right one block
    } else if (key == "ArrowLeft") {
        pacManLeft -= 26 // move left one block
    } else if (key == "ArrowUp") {
        pacManTop -= 26 // subtract because it is distance from the top, move up
    } else if (key == "ArrowDown") {
        pacManTop += 26 // add because it is distance from the top, move down
    }

    displayPacMan(pacManLeft, pacManTop) // update display
}
