// Get the canvas element
const canvas = document.getElementById("moireCanvas")
const ctx = canvas.getContext("2d")

// Set the canvas dimensions
canvas.width = window.innerWidth
canvas.height = window.innerHeight

// Pattern properties
const patternSize = 100 // Size of the individual pattern elements
const patternSpacing = 20 // Spacing between the pattern elements

// Animation variables
let rotationAngle = 0
const rotationSpeed = 0.01

// Function to generate a single pattern
function generatePattern(xOffset, yOffset, rotation) {
    ctx.save()
    ctx.translate(xOffset, yOffset)
    ctx.rotate(rotation)

    ctx.beginPath()
    ctx.moveTo(-patternSize / 2, -patternSize / 2)
    ctx.lineTo(patternSize / 2, -patternSize / 2)
    ctx.lineTo(patternSize / 2, patternSize / 2)
    ctx.lineTo(-patternSize / 2, patternSize / 2)
    ctx.closePath()

    ctx.strokeStyle = "#FFF"
    ctx.lineWidth = 2
    ctx.stroke()

    ctx.restore()
}

// Function to generate the Moiré pattern
function generateMoirePattern() {
    ctx.clearRect(0, 0, canvas.width, canvas.height)

    const patternCountX = Math.ceil(canvas.width / patternSpacing)
    const patternCountY = Math.ceil(canvas.height / patternSpacing)

    for (let i = 0; i < patternCountX; i++) {
        for (let j = 0; j < patternCountY; j++) {
            const xOffset = i * patternSpacing
            const yOffset = j * patternSpacing
            const rotation = (i + j) % 2 === 0 ? rotationAngle : -rotationAngle

            generatePattern(xOffset, yOffset, rotation)
        }
    }
}

// Animation loop
function animate() {
    // Update the rotation angle
    rotationAngle += rotationSpeed

    // Generate and draw the Moiré pattern
    generateMoirePattern()

    // Request the next animation frame
    requestAnimationFrame(animate)
}

// Start the animation
animate()
