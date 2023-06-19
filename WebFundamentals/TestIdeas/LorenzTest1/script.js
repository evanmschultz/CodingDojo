// Get the canvas element
const canvas = document.getElementById("lorenzCanvas")
const ctx = canvas.getContext("2d")

// Set the canvas dimensions
canvas.width = window.innerWidth
canvas.height = window.innerHeight

// Set the initial parameters
const rho = 35
const sigma = 8
const beta = 8 / 3
let x = 0.01
let y = 0
let z = 0
const dt = 0.01

// Set the colors
const lineColor = "rgb(255, 255, 255)"
const pointColor = "rgb(255, 0, 0)"

// Function to update the position
function updatePosition() {
    const dx = sigma * (y - x)
    const dy = x * (rho - z) - y
    const dz = x * y - beta * z

    x += dx * dt
    y += dy * dt
    z += dz * dt
}

// Function to draw the Lorenz attractor
function drawLorenz() {
    const scale = 10
    const xOffset = canvas.width / 2
    const yOffset = canvas.height / 2

    ctx.beginPath()
    ctx.moveTo(xOffset + scale * x, yOffset + scale * y)

    // Update and draw the position for a specified number of steps
    for (let i = 0; i < 10000; i++) {
        updatePosition()
        ctx.lineTo(xOffset + scale * x, yOffset + scale * y)
    }

    ctx.strokeStyle = lineColor
    ctx.stroke()
    ctx.fillStyle = pointColor
    ctx.fillRect(xOffset + scale * x - 2, yOffset + scale * y - 2, 4, 4)
}

// Animation loop
function animate() {
    // Clear the canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height)

    // Draw the Lorenz attractor
    drawLorenz()

    // Request the next animation frame
    requestAnimationFrame(animate)
}

// Start the animation
animate()
