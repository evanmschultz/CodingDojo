/* Credit for most of the code goes to Gary Ang - https://github.com/playgrdstar/lorenz_threejs */

// Grab the canvas from the HTML document
var myCanvas = document.getElementById("myCanvas")

// Setting up the scene
var scene = new THREE.Scene()

// Setting up a camera
var camera = new THREE.PerspectiveCamera(
    100,
    myCanvas.clientWidth / myCanvas.clientHeight,
    0.1,
    50
)
camera.position.z = 30

// Setting up the renderer. This will be called later to render scene with the camera setup above
var renderer = new THREE.WebGLRenderer({
    antialias: true,
    canvas: myCanvas, // Pass the canvas element to the renderer
})
renderer.setPixelRatio(window.devicePixelRatio)
renderer.setSize(myCanvas.clientWidth, myCanvas.clientHeight)
renderer.setClearColor(0x111111, 1)

// Setting up a light
var light = new THREE.PointLight("#9BC995", 1, 1000)
light.position.set(0, 0, 0)
scene.add(light)

// Setting up a group to hold the items we will be creating together
var group = new THREE.Group()

// Array curve holds the positions of points generated from a lorenz equation; lorenz function below generates the points and returns an array of points
var arrayCurve = lorenz()

// Generating the geometry
var curve = new THREE.CatmullRomCurve3(arrayCurve)
var geometry = new THREE.BufferGeometry().setFromPoints(curve.getPoints(100000))

// Generating a cloud of points
var pcMat = new THREE.PointsMaterial({
    color: new THREE.Color(0x999ccc),
    transparent: true,
    size: 0.05,
    blending: THREE.AdditiveBlending,
})
var pc = new THREE.Points(geometry, pcMat)
pc.sizeAttenuation = true
pc.sortPoints = true
group.add(pc)
scene.add(group)

var prevFog = true
var step = 0
var render = function () {
    renderer.render(scene, camera)
    requestAnimationFrame(render)

    //Varying the points on each frame
    step += 0.01
    var count = 0
    var geometry = pc.geometry
    var a = 0.9 + Math.random() * 6
    var b = 3.4 + Math.random() * 7
    var f = 9.9 + Math.random() * 8
    var g = 1 + Math.random()
    var t = 0.001

    var positions = geometry.attributes.position.array
    var index = 0
    for (let i = 0; i < positions.length; i += 3) {
        var x = positions[i]
        var y = positions[i + 1]
        var z = positions[i + 2]
        positions[i] = x - t * a * x + t * y * y - t * z * z + t * a * f
        positions[i + 1] = y - t * y + t * x * y - t * b * x * z + t * g
        positions[i + 2] = z - t * z + t * b * x * y + t * x * z
    }
    geometry.attributes.position.needsUpdate = true

    group.rotation.x += 0.01
    group.rotation.y += 0.02
    group.rotation.z += 0.01
}

window.addEventListener(
    "resize",
    function () {
        camera.aspect = myCanvas.clientWidth / myCanvas.clientHeight
        camera.updateProjectionMatrix()
        renderer.setSize(myCanvas.clientWidth, myCanvas.clientHeight)
    },
    false
)

render()

function lorenz() {
    var arrayCurve = []
    var x = 0.1,
        y = 0.1,
        z = 0.1
    var a = 0.2
    var b = 3.4
    var f = 9.9
    var g = 1
    var t = 0.001
    for (var i = 0; i < 100000; i++) {
        var x1 = x
        var y1 = y
        var z1 = z
        x = x - t * a * x + t * y * y - t * z * z + t * a * f
        y = y - t * y + t * x * y - t * b * x * z + t * g
        z = z - t * z + t * b * x * y + t * x * z
        arrayCurve.push(new THREE.Vector3(x, y, z).multiplyScalar(1))
    }
    return arrayCurve
}
