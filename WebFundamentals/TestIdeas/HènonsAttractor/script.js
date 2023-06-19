const canvas = document.getElementById("canvas")
const context = canvas.getContext("2d")
const devicePixelRatio = window.devicePixelRatio || 1

// scale canvas in actual pixels for high-DPI devices
canvas.width = 2000 * devicePixelRatio
canvas.height = 2000 * devicePixelRatio

// set dot color
context.fillStyle = "#ddd"

// Initial values
let x = 0.1,
    y = 0.1

// Constants for the Hénon Map
const a = 1.41,
    b = 0.3,
    changeCount = 2999
let count = 0
// let colorChangeCount

// Function to calculate next point
function henon(x, y) {
    return [y + 1 - a * x * x, b * x]
}

// Precalculate to get the bounds
let minX = x,
    maxX = x,
    minY = y,
    maxY = y
for (let i = 0; i < 1000; i++) {
    ;[x, y] = henon(x, y)
    minX = Math.min(minX, x)
    maxX = Math.max(maxX, x)
    minY = Math.min(minY, y)
    maxY = Math.max(maxY, y)
}

// Calculate scale and shift factors to fit the attractor to the canvas
const scaleX = canvas.width / (maxX - minX) - 100
const scaleY = canvas.height / (maxY - minY) - 100
const shiftX = -minX * scaleX + 100
const shiftY = -minY * scaleY

// Reset initial values
x = 1
y = 1

// Update the canvas every 1ms
setInterval(function () {
    // Calculate next point
    ;[x, y] = henon(x, y)

    // Plot point on the canvas
    context.fillRect(shiftX + x * scaleX, shiftY + y * scaleY, 5, 5)

    count++
    if (count % changeCount == 0) {
        console.log("changeCount hit")
        if (count % 2 == 0) {
            context.fillStyle = "#ddd"
            console.log(context.fillStyle)
        } else {
            context.fillStyle = "#fff"
            console.log(context.fillStyle)
        }
    }
    if (count == 20000) {
        console.log("stopping js animation")
        return
    }
}, 1)
