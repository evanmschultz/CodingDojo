let scene = new THREE.Scene()
let camera = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1)

let shader = {
    uniforms: {
        zoom: { type: "f", value: 1.0 },
        offset: {
            type: "v2",
            value: new THREE.Vector2(0.75001, -0.02),
        },
    },
    vertexShader: [
        "varying vec2 vUv;",
        "void main() {",
        "vUv = uv;",
        "gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);",
        "}",
    ].join("\n"),
    fragmentShader: [
        "uniform float zoom;",
        "uniform vec2 offset;",
        "varying vec2 vUv;",
        "void main() {",
        "vec2 c = (vUv - vec2(0.5, 0.5)) * 4.0 / zoom - offset;",
        "vec2 z = vec2(0.0, 0.0);",
        "float n = 0.0;",
        "for (int i = 0; i < 300; i++) {",
        "if(dot(z, z) > 4.0) {",
        "n = float(i) / 300.0;",
        "break;",
        "}",
        "z = vec2(z.x*z.x - z.y*z.y, 2.0*z.x*z.y) + c;",
        "}",
        "gl_FragColor = vec4(vec3(n, n, n), 1.0);",
        "}",
    ].join("\n"),
}

let geometry = new THREE.PlaneBufferGeometry(2, 2)
let material = new THREE.ShaderMaterial(shader)
let mesh = new THREE.Mesh(geometry, material)
scene.add(mesh)

let renderer = new THREE.WebGLRenderer()
renderer.setSize(window.innerWidth, window.innerHeight)
document.body.appendChild(renderer.domElement)

let animate = function () {
    shader.uniforms.zoom.value *= 1.01
    requestAnimationFrame(animate)
    renderer.render(scene, camera)
}
animate()
