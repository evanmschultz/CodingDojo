let world = [
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 1, 0, 2, 1, 2, 0, 1, 0, 0],
    [2, 2, 0, 2, 0, 0, 0, 2, 2, 2],
    [2, 2, 0, 2, 2, 2, 0, 2, 1, 2],
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
