// Get the canvas element
const canvas = document.getElementById("psoCanvas")
const ctx = canvas.getContext("2d")

// Set the canvas dimensions
canvas.width = window.innerWidth
canvas.height = window.innerHeight

// Particle properties
const numParticles = 1000 // Number of particles
const particleSize = 1 // Size of particles
const maxVelocity = 1 // Maximum velocity of particles

// Optimization problem properties
const targetX = canvas.width / 2 // X coordinate of the target position
const targetY = canvas.height / 2 // Y coordinate of the target position

// Particle Swarm Optimization algorithm
const particles = []

// Create particles
for (let i = 0; i < numParticles; i++) {
    const particle = {
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        velocityX: Math.random() * maxVelocity * 2 - maxVelocity,
        velocityY: Math.random() * maxVelocity * 2 - maxVelocity,
        bestX: null,
        bestY: null,
        bestDistance: Infinity,
    }

    particles.push(particle)
}

// Function to calculate the distance between two points
function calculateDistance(x1, y1, x2, y2) {
    const dx = x2 - x1
    const dy = y2 - y1
    return Math.sqrt(dx * dx + dy * dy)
}

// Animation loop
function animate() {
    // Clear the canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height)

    // Update particles
    particles.forEach((particle) => {
        const { x, y, velocityX, velocityY, bestX, bestY, bestDistance } =
            particle

        // Update position
        particle.x += velocityX
        particle.y += velocityY

        // Reflect off the edges of the canvas
        if (particle.x < 0 || particle.x > canvas.width) {
            particle.velocityX *= -1
        }
        if (particle.y < 0 || particle.y > canvas.height) {
            particle.velocityY *= -1
        }

        // Calculate distance to the target
        const distanceToTarget = calculateDistance(x, y, targetX, targetY)

        // Update personal best position if necessary
        if (distanceToTarget < bestDistance) {
            particle.bestX = x
            particle.bestY = y
            particle.bestDistance = distanceToTarget
        }

        // Draw the particle
        ctx.fillStyle = "#FFF"
        ctx.fillRect(
            x - particleSize / 2,
            y - particleSize / 2,
            particleSize,
            particleSize
        )
    })

    // Draw the target
    ctx.fillStyle = "#FF0000"
    ctx.fillRect(
        targetX - particleSize / 2,
        targetY - particleSize / 2,
        particleSize,
        particleSize
    )

    // Request the next animation frame
    requestAnimationFrame(animate)
}

// Start the animation
animate()
