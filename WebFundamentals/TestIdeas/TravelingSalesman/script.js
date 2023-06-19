// Get the canvas element
const canvas = document.getElementById("tspCanvas")
const ctx = canvas.getContext("2d")

// Set the canvas dimensions
canvas.width = window.innerWidth
canvas.height = window.innerHeight

// TSP properties
const numCities = 10 // Number of cities
const cityRadius = 5 // Radius of cities

// Generate random cities
function generateRandomCities() {
    const cities = []
    for (let i = 0; i < numCities; i++) {
        const x = Math.random() * (canvas.width - 100) + 50
        const y = Math.random() * (canvas.height - 100) + 50
        cities.push({ x, y })
    }
    return cities
}

// Calculate the distance between two cities
function calculateDistance(city1, city2) {
    const dx = city2.x - city1.x
    const dy = city2.y - city1.y
    return Math.sqrt(dx * dx + dy * dy)
}

// Calculate the total distance of a given route
function calculateTotalDistance(route) {
    let totalDistance = 0
    for (let i = 0; i < route.length - 1; i++) {
        totalDistance += calculateDistance(route[i], route[i + 1])
    }
    return totalDistance
}

// Generate initial random route
let cities = generateRandomCities()
let currentRoute = cities.slice()

// Function to draw the current route
function drawRoute() {
    ctx.clearRect(0, 0, canvas.width, canvas.height)

    // Draw the cities
    ctx.fillStyle = "#FFF"
    cities.forEach((city) => {
        ctx.beginPath()
        ctx.arc(city.x, city.y, cityRadius, 0, 2 * Math.PI)
        ctx.fill()
    })

    // Draw the route
    ctx.strokeStyle = "#FFF"
    ctx.lineWidth = 2
    ctx.beginPath()
    ctx.moveTo(currentRoute[0].x, currentRoute[0].y)
    for (let i = 1; i < currentRoute.length; i++) {
        ctx.lineTo(currentRoute[i].x, currentRoute[i].y)
    }
    ctx.closePath()
    ctx.stroke()
}

// 2-opt optimization algorithm
function twoOpt() {
    let improved = true
    while (improved) {
        improved = false
        for (let i = 0; i < currentRoute.length - 2; i++) {
            for (let j = i + 2; j < currentRoute.length; j++) {
                const distance1 = calculateDistance(
                    currentRoute[i],
                    currentRoute[i + 1]
                )
                const distance2 = calculateDistance(
                    currentRoute[j],
                    currentRoute[(j + 1) % numCities]
                )
                const newDistance1 = calculateDistance(
                    currentRoute[i],
                    currentRoute[j]
                )
                const newDistance2 = calculateDistance(
                    currentRoute[i + 1],
                    currentRoute[(j + 1) % numCities]
                )

                if (newDistance1 + newDistance2 < distance1 + distance2) {
                    currentRoute.splice(
                        i + 1,
                        j - i,
                        ...currentRoute.slice(i + 1, j).reverse()
                    )
                    improved = true
                }
            }
        }
    }
}

// Animation loop
function animateTSP() {
    drawRoute()
    twoOpt()

    // Request the next animation frame
    requestAnimationFrame(animateTSP)
}

// Start the TSP animation
animateTSP()
