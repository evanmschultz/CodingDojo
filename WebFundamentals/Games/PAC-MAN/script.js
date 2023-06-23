let world = [
	[2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
	[2, 1, 0, 2, 1, 2, 0, 1, 0, 0],
	[2, 2, 0, 2, 0, 0, 0, 2, 2, 2],
	[2, 2, 0, 0, 2, 2, 0, 2, 1, 2],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
	[2, 0, 0, 0, 2, 0, 0, 0, 2, 2],
	[2, 2, 2, 2, 0, 1, 2, 0, 0, 2],
	[2, 1, 0, 0, 0, 0, 2, 0, 1, 2],
	[2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
]

function displayWorld() {
	let output = ''

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

		output += '</div>\n' // close row tag
	}
	// console.log(output)
	document.getElementById('world').innerHTML = output // pass output to document
}
displayWorld()

let pacmanPosition = {
	x: 0,
	y: 4
}
function displayPacman(x, y) {
	// named with let to make it clear it is being updated
	let pacman = document.getElementById('pac-man')

	// update current position in position object
	pacmanPosition.x = x
	pacmanPosition.y = y

	// update the styling
	pacman.style.top = `${pacmanPosition.y * 26 + 3}px`
	pacman.style.left = `${pacmanPosition.x * 26 + 3}px`

	checkForCoin()
}
// set pacman starting position
displayPacman(pacmanPosition.x, pacmanPosition.y)

let ghostPosition = {
	x: 5,
	y: 4
}
function displayGhost() {
	let ghost1 = document.getElementById('ghost1')

	ghost1.style.backgroundImage = 'url(Assets/ghost1.png)'

	ghost1.style.top = `${ghostPosition.y * 26 + 3}px`
	ghost1.style.left = `${ghostPosition.x * 26 + 3}px`
}

const ghostDirectionOptions = ['left', 'right', 'up', 'down']
function moveGhost() {
	const directionIndex = Math.round(
		Math.random() * ghostDirectionOptions.length
	)
	const direction = ghostDirectionOptions[directionIndex]
	let ghostY = ghostPosition.y
	let ghostX = ghostPosition.x

	if (
		direction == 'left' &&
		checkForCollision(ghostY, ghostX - 1) &&
		ghostX - 1 >= 0
	) {
		ghostX--
	} else if (
		direction == 'right' &&
		checkForCollision(ghostY, ghostX + 1) &&
		ghostX + 1 < world[0].length
	) {
		ghostX++
	} else if (direction == 'up' && checkForCollision(ghostY - 1, ghostX)) {
		ghostY--
	} else if (direction == 'down' && checkForCollision(ghostY + 1, ghostX)) {
		ghostY++
	} else {
		moveGhost()
	}

	ghostPosition.y = ghostY
	ghostPosition.x = ghostX
	displayGhost()
}

setTimeout(() => {
	displayGhost()
	setInterval(moveGhost, 500)
}, 1000)

let score = 0
function checkForCoin() {
	const pacmanX = pacmanPosition.x
	const pacmanY = pacmanPosition.y

	if (world[pacmanY][pacmanX] == 1) {
		let scoreDisplay = document.getElementById('coin-count')
		score += 10

		scoreDisplay.innerText = `Coin Count: ${score}` // update count on screen

		world[pacmanY][pacmanX] = 0 // remove coin

		displayWorld() // refresh world
	}
}

function checkForCollision(y, x) {
	if (world[y][x] != 2) {
		return true
	}
	return false
}

// control pacman movement
document.onkeydown = function (event) {
	const key = event.key

	// get the integer value of the current position
	let pacmanX = pacmanPosition.x
	let pacmanY = pacmanPosition.y

	if (
		key == 'ArrowRight' &&
		checkForCollision(pacmanY, pacmanX + 1) &&
		pacmanX + 1 <= world[0].length
	) {
		pacmanX++

		// check if leaving maze
		if (pacmanX > world[0].length - 1) {
			console.log('map complete')
		}
	} else if (
		key == 'ArrowLeft' &&
		checkForCollision(pacmanY, pacmanX - 1) &&
		pacmanX - 1 >= 0
	) {
		// subtract one to check for collision move left one, displayPacman()
		pacmanX--
	} else if (key == 'ArrowUp' && checkForCollision(pacmanY - 1, pacmanX)) {
		// subtract because it is distance from the top, move up
		pacmanY--
	} else if (key == 'ArrowDown' && checkForCollision(pacmanY + 1, pacmanX)) {
		// add because it is distance from the top, move down
		pacmanY++
	}

	displayPacman(pacmanX, pacmanY) // update display
}

// refactor to have a function that checks collision so it works for the ghost as well
// add displayGhost() with timer that moves it
// make pacman turn direction of travel
// add cherry, worth 50 points, change coins to be worth 10, change coin count to score
