// Get the canvas element
const canvas = document.getElementById("flockingCanvas")
const ctx = canvas.getContext("2d")

// Set the canvas dimensions
canvas.width = window.innerWidth
canvas.height = window.innerHeight

// Parameters for the Boids algorithm
const numBoids = 2000 // Number of boids
const maxSpeed = 2 // Maximum speed of boids
const perceptionRadius = 50 // Radius within which boids perceive neighbors
const separationWeight = 3 // Weight for separation behavior
const alignmentWeight = 2 // Weight for alignment behavior
const cohesionWeight = 3 // Weight for cohesion behavior
const randomDirectionProbability = 1 // Probability of moving in a random direction

// Boid properties
const boids = []
for (let i = 0; i < numBoids; i++) {
    const x = Math.random() * canvas.width
    const y = Math.random() * canvas.height
    const dx = Math.random() * 2 - 1
    const dy = Math.random() * 2 - 1
    boids.push({ x, y, dx, dy })
}

// Function to update and draw the boids
function updateBoids() {
    ctx.clearRect(0, 0, canvas.width, canvas.height)

    for (let i = 0; i < numBoids; i++) {
        const boid = boids[i]

        // Separation behavior
        let separationX = 0
        let separationY = 0
        let separationCount = 0

        // Alignment behavior
        let alignmentX = 0
        let alignmentY = 0
        let alignmentCount = 0

        // Cohesion behavior
        let cohesionX = 0
        let cohesionY = 0
        let cohesionCount = 0

        // Iterate over all other boids
        for (let j = 0; j < numBoids; j++) {
            if (i !== j) {
                const otherBoid = boids[j]
                const distance = Math.sqrt(
                    (boid.x - otherBoid.x) ** 2 + (boid.y - otherBoid.y) ** 2
                )

                // Separation behavior: steer away from nearby boids
                if (distance < perceptionRadius) {
                    separationX += (boid.x - otherBoid.x) / distance
                    separationY += (boid.y - otherBoid.y) / distance
                    separationCount++
                }

                // Alignment behavior: steer towards the average heading of nearby boids
                if (distance < perceptionRadius) {
                    alignmentX += otherBoid.dx
                    alignmentY += otherBoid.dy
                    alignmentCount++
                }

                // Cohesion behavior: steer towards the average position of nearby boids
                if (distance < perceptionRadius) {
                    cohesionX += otherBoid.x
                    cohesionY += otherBoid.y
                    cohesionCount++
                }
            }
        }

        // Calculate average separation, alignment, and cohesion vectors
        if (separationCount > 0) {
            separationX /= separationCount
            separationY /= separationCount
        }
        if (alignmentCount > 0) {
            alignmentX /= alignmentCount
            alignmentY /= alignmentCount
        }
        if (cohesionCount > 0) {
            cohesionX /= cohesionCount
            cohesionY /= cohesionCount
        }

        // Update boid velocity based on the three behaviors
        boid.dx +=
            separationX * separationWeight +
            alignmentX * alignmentWeight +
            cohesionX * cohesionWeight

        boid.dy +=
            separationY * separationWeight +
            alignmentY * alignmentWeight +
            cohesionY * cohesionWeight

        // Random movement if not near other boids
        if (
            separationCount === 0 &&
            alignmentCount === 0 &&
            cohesionCount === 0
        ) {
            if (Math.random() < randomDirectionProbability) {
                boid.dx = Math.random() * 2 - 1
                boid.dy = Math.random() * 2 - 1
            }
        }

        // Limit boid speed
        const speed = Math.sqrt(boid.dx ** 2 + boid.dy ** 2)
        if (speed > maxSpeed) {
            boid.dx = (boid.dx / speed) * maxSpeed
            boid.dy = (boid.dy / speed) * maxSpeed
        }

        // Update boid position
        boid.x += boid.dx
        boid.y += boid.dy

        // Wrap around the canvas boundaries
        if (boid.x > canvas.width) {
            boid.x = 0
        } else if (boid.x < 0) {
            boid.x = canvas.width
        }
        if (boid.y > canvas.height) {
            boid.y = 0
        } else if (boid.y < 0) {
            boid.y = canvas.height
        }

        // Draw boid
        ctx.beginPath()
        ctx.arc(boid.x, boid.y, 0.5, 0, 2 * Math.PI)
        ctx.fillStyle = "#FFF"
        ctx.fill()
    }
}

// Animation loop
function animate() {
    updateBoids()
    requestAnimationFrame(animate)
}

// Start the animation
animate()
