const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / 300, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({
    canvas: document.getElementById("three-js-animation"),
    alpha: true,
    antialias: true
});
renderer.setClearColor(0x000000, 0);
renderer.setSize(window.innerWidth / 2, 200);

const cubes = [];
const numCubes = 7;
const radius = 2;

for (let i = 0; i < numCubes; i++) {
    const size = 1;
    const geometry = new THREE.BoxGeometry(size, size, size);

    const pastelColors = [0xFFB6C1, 0xAED6F1, 0xFAD7A0, 0xD5F5E3, 0xF9E79F];
    const color = pastelColors[i % pastelColors.length];
    const material = new THREE.MeshLambertMaterial({ color: color });

    const cube = new THREE.Mesh(geometry, material);

    const angle = (i / numCubes) * Math.PI * 2;
    const height = i * 0.5 - (numCubes * 0.25);

    cube.position.x = Math.cos(angle) * radius * 2;
    cube.position.z = Math.sin(angle) * radius;
    cube.position.y = height;
    scene.add(cube);
    cubes.push({
        mesh: cube,
        angle: angle
    });
}

const light = new THREE.PointLight(0xffffff, 1, 100);
light.position.set(10, 10, 10);
scene.add(light);

camera.position.z = 5;

let time = 0;

function animate() {
    requestAnimationFrame(animate);

    time += 0.005;

    cubes.forEach(cubeObj => {
        cubeObj.mesh.rotation.x += 0.01;
        cubeObj.mesh.rotation.y += 0.01;

        cubeObj.mesh.position.y = Math.tan(cubeObj.angle + time) * 4;
    });

    renderer.render(scene, camera);
}
animate();
