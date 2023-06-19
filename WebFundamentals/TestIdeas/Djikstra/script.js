// Get the canvas element
const canvas = document.getElementById("dijkstraCanvas")
const ctx = canvas.getContext("2d")

// Set the canvas dimensions
canvas.width = window.innerWidth
canvas.height = window.innerHeight

// Graph properties
const numNodes = 7 // Number of nodes in the graph
const minDistance = 50 // Minimum distance between nodes
const maxDistance = 200 // Maximum distance between nodes

// Generate random graph
const nodes = []
for (let i = 0; i < numNodes; i++) {
    const x = Math.random() * canvas.width
    const y = Math.random() * canvas.height
    nodes.push({
        x,
        y,
        index: i,
        distance: Infinity,
        visited: false,
    })
}

// Generate random edges
const edges = []
for (let i = 0; i < numNodes; i++) {
    for (let j = i + 1; j < numNodes; j++) {
        const distance =
            minDistance + Math.random() * (maxDistance - minDistance)
        edges.push([i, j, distance])
        edges.push([j, i, distance])
    }
}

// Animation variables
const animationSpeed = 20 // Speed of animation in milliseconds

// Function to draw the graph
function drawGraph() {
    ctx.clearRect(0, 0, canvas.width, canvas.height)

    // Draw edges
    for (let i = 0; i < edges.length; i++) {
        const [u, v, weight] = edges[i]
        const { x: x1, y: y1 } = nodes[u]
        const { x: x2, y: y2 } = nodes[v]

        ctx.beginPath()
        ctx.moveTo(x1, y1)
        ctx.lineTo(x2, y2)
        ctx.strokeStyle = "#FFF"
        ctx.lineWidth = 2
        ctx.stroke()

        // Draw edge weight
        const textX = (x1 + x2) / 2
        const textY = (y1 + y2) / 2
        ctx.fillStyle = "#FFF"
        ctx.fillText(weight.toString(), textX, textY)
    }

    // Draw vertices
    for (let i = 0; i < nodes.length; i++) {
        const { x, y } = nodes[i]

        ctx.beginPath()
        ctx.arc(x, y, 5, 0, 2 * Math.PI)
        ctx.fillStyle = "#FFF"
        ctx.fill()
    }
}

// Function to animate Dijkstra's algorithm
function animateDijkstra() {
    // Reset nodes
    for (let i = 0; i < nodes.length; i++) {
        nodes[i].distance = Infinity
        nodes[i].visited = false
    }
    nodes[0].distance = 0

    // Animation loop
    const animationLoop = setInterval(() => {
        // Find the node with the minimum distance
        let minDistance = Infinity
        let minNodeIndex = -1
        for (let i = 0; i < nodes.length; i++) {
            const { distance, visited } = nodes[i]
            if (!visited && distance < minDistance) {
                minDistance = distance
                minNodeIndex = i
            }
        }

        // If all nodes have been visited or unreachable, stop the animation
        if (minNodeIndex === -1) {
            clearInterval(animationLoop)
            return
        }

        const minNode = nodes[minNodeIndex]
        minNode.visited = true

        // Update the distances of adjacent nodes
        for (let i = 0; i < edges.length; i++) {
            const [u, v, weight] = edges[i]
            if (u === minNode.index) {
                const adjacentNode = nodes[v]
                const newDistance = minNode.distance + weight
                if (newDistance < adjacentNode.distance) {
                    adjacentNode.distance = newDistance
                }
            } else if (v === minNode.index) {
                const adjacentNode = nodes[u]
                const newDistance = minNode.distance + weight
                if (newDistance < adjacentNode.distance) {
                    adjacentNode.distance = newDistance
                }
            }
        }

        // Draw the updated graph
        drawGraph()

        // Highlight the visited and unvisited nodes
        for (let i = 0; i < nodes.length; i++) {
            const { x, y, visited } = nodes[i]
            ctx.beginPath()
            ctx.arc(x, y, 5, 0, 2 * Math.PI)
            ctx.fillStyle = visited ? "#00FF00" : "#FF0000"
            ctx.fill()
        }
    }, animationSpeed)
}

// Start the animation of Dijkstra's algorithm
animateDijkstra()
