// Get the canvas element
const canvas = document.getElementById("mazeCanvas")
const ctx = canvas.getContext("2d")

// Set the canvas dimensions
canvas.width = window.innerWidth
canvas.height = window.innerHeight

// Maze properties
const cellSize = 20 // Size of each cell in pixels
const mazeWidth = Math.floor(canvas.width / cellSize)
const mazeHeight = Math.floor(canvas.height / cellSize)

// Maze grid
const grid = Array(mazeHeight)
    .fill(null)
    .map(() => Array(mazeWidth).fill(true))

// Function to draw the maze grid
function drawMaze() {
    ctx.clearRect(0, 0, canvas.width, canvas.height)

    for (let row = 0; row < mazeHeight; row++) {
        for (let col = 0; col < mazeWidth; col++) {
            const x = col * cellSize
            const y = row * cellSize

            if (grid[row][col]) {
                ctx.fillStyle = "#FFF"
                ctx.fillRect(x, y, cellSize, cellSize)
            }
        }
    }
}

// Recursive Backtracking algorithm
function recursiveBacktracking(row, col) {
    const directions = [
        { dx: 0, dy: -1 }, // Up
        { dx: 1, dy: 0 }, // Right
        { dx: 0, dy: 1 }, // Down
        { dx: -1, dy: 0 }, // Left
    ]

    // Shuffle the directions randomly
    for (let i = directions.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1))
        ;[directions[i], directions[j]] = [directions[j], directions[i]]
    }

    const animationLoop = setInterval(() => {
        let validDirectionFound = false

        for (let i = 0; i < directions.length; i++) {
            const { dx, dy } = directions[i]
            const nextRow = row + dy * 2
            const nextCol = col + dx * 2

            if (
                nextRow >= 0 &&
                nextRow < mazeHeight &&
                nextCol >= 0 &&
                nextCol < mazeWidth &&
                grid[nextRow][nextCol]
            ) {
                grid[row + dy][col + dx] = false
                grid[nextRow][nextCol] = false

                drawMaze()

                validDirectionFound = true
                recursiveBacktracking(nextRow, nextCol)
                break
            }
        }

        if (!validDirectionFound) {
            clearInterval(animationLoop)
        }
    }, 50)
}

// Start the maze generation
recursiveBacktracking(0, 0)
