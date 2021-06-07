// Load synth model

const loader = new THREE.GLTFLoader();

loader.load(
   "./library/Synth.glb",
   function ( gltf ) {
      synth = gltf.scene;
      synth.name = 'synth';
      scene.add(synth);
      scene.getObjectByName('Screen').material = new THREE.MeshBasicMaterial( { color: 0x000000 } );
   },
);

// Misc funtions
function getRandomFloat(min, max) {
    return Math.random() * (max - min + 1) + min;
}

// Functions for converting rgb values to hex from https://krazydad.com/tutorials/makecolors.php
function byte2Hex(n)
  {
    var nybHexString = "0123456789ABCDEF";
    return String(nybHexString.substr((n >> 4) & 0x0F,1)) + nybHexString.substr(n & 0x0F,1);
  }

function RGB2Color(r,g,b)
  {
    return '#' + byte2Hex(r) + byte2Hex(g) + byte2Hex(b);
}

function getRainbow(mouseValY, mouseValX, frequency1, frequency2, frequency3,
                               phase1, phase2, phase3,
                               center, width, len)
  {
    if (center == undefined)   center = 128;
    if (width == undefined)    width = 127;
    if (len == undefined)      len = 50;

    var red = Math.sin(frequency1*mouseValY + phase1) * width + center;
    var grn = Math.sin(frequency2*mouseValX + phase2) * width + center;
    var blu = Math.sin(frequency3*mouseValY + phase3) * width + center;
    return(RGB2Color(red,grn,blu));

  }

// Set up scene and camera
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );

const renderer = new THREE.WebGLRenderer({ antialias: true});
renderer.setSize( window.innerWidth, window.innerHeight );
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap; // default THREE.PCFShadowMap
document.body.appendChild( renderer.domElement );
scene.background = new THREE.Color(0x7C9885);


// Do the lights

const light = new THREE.DirectionalLight( 0xffffff , 5);
light.position.set( 0, 0, -5 );
light.castShadow = true;

scene.add( light );

const amblight = new THREE.AmbientLight( 0x7C9885, 1 ); // soft white light
scene.add( amblight );

const directionalLight = new THREE.DirectionalLight( 0xffffff, 4 );
directionalLight.position.x = 2;
directionalLight.castShadow = true;

scene.add( directionalLight );

// Do some variable setting and making

camera.position.z = 1;
camera.position.y = 4;
camera.rotation.x = -20.1;

var COLOURS = [0xFC7753, 0xA288E3, 0x7D1D3F]

var squareBArr = [];
var squareBAmt = 3;
var mouse = new THREE.Vector2();
var raycaster =  new THREE.Raycaster();
var heldMouse = new THREE.Vector2();
var changeColour;
var isMoving;
var oldkey;
var slideTri = 0;
var curBall;
var readyMate;



// Set Tone.JS variables and synths

// Objects for visualisation
const toneFFT = new Tone.FFT();
toneFFT.smoothing = 0.1;
toneFFT.normalRange = true;

const toneWaveform = new Tone.Waveform();
toneWaveform.size = 512;


const meter1 = new Tone.DCMeter();
const meter2 = new Tone.DCMeter();

// Sound effects
const filter = new Tone.Filter(15000, "lowpass").toDestination();
filter.rolloff = -48;
filter.q = 5;

const freeverb = new Tone.Freeverb().toDestination().connect(toneFFT);
freeverb.dampening = 3000;
freeverb.roomSize.value = 0.8;

const chorus = new Tone.Chorus(1, 2.5, 0.5).start();

const crossFade2 = new Tone.CrossFade().connect(filter).connect(toneFFT).connect(toneWaveform);
const crossFade = new Tone.CrossFade().connect(crossFade2.a);

// Synths
const fmSynth1 = new Tone.FMSynth({
    harmonicity: 1,
    detune: 0,
    modulationIndex: 20,
    oscillator: {
        type: "square"
    },
    envelope: {
        attack: 0.01,
        decay: 0.01,
        sustain: 1,
        release: 0.5
    },
    modulation: {
      type: "sawtooth",
    }

}).connect(crossFade.a).connect(meter1);
fmSynth1.volume.value = -10

const fmSynth2 = new Tone.FMSynth({
    harmonicity: 1,
    detune: 0,
    modulationIndex: 20,
    oscillator: {
        type: "sine"
    },
    envelope: {
        attack: 0.01,
        decay: 0.01,
        sustain: 1,
        release: 0.5
    },
    modulation: {
      type: "sawtooth",
    }

}).connect(crossFade.b).connect(meter2);
fmSynth2.volume.value = -10

const pluckSynth = new Tone.PluckSynth({
  resonance: 0.98,
  dampening: 4000
}).connect(crossFade2.b);
pluckSynth.volume.value = -10

// A few fx settings that had to be done afterwards
crossFade.connect(chorus).connect(freeverb);
crossFade.fade.value = 0.5;
crossFade2.fade.value = 0.5;

// Class for Square Ball getCanvasElementSize
let blobCounter = 1;

class SquareBlob {

  constructor() {
    this.sBMaterial = new THREE.MeshBasicMaterial( { color: COLOURS[Math.floor(Math.random() * COLOURS.length)] } );
    this.firstSphere = new THREE.SphereGeometry(0.06, 10, 8);
    this.sphere = new THREE.Mesh( this.firstSphere, this.sBMaterial );
    this.sphere.name = 'Balletje' + blobCounter;
    this.sphere.position.set(Math.min(Math.max(getRandomFloat(-2.28, -1.5), -2.28), -1.5),Math.min(Math.max(getRandomFloat(0.56, 0.68), 0.56), 0.68),Math.min(Math.max(getRandomFloat(-1.44, -0.59), -1.44), -0.59));
    blobCounter += 1;
    scene.add( this.sphere );
  }
};

for (i = 0; i < squareBAmt; i++) {
  squareBArr.push(new SquareBlob);
}

// Create the visualiser torus
const torGeometry = new THREE.TorusGeometry( 5, 0.4, 4, 18 );
const torMaterial = new THREE.PointsMaterial({
  size: 0.05,
  color: 0xA288E3
});
const torus = new THREE.Mesh( torGeometry, torMaterial );
torus.name = 'Visualiser';
torus.position.z = -0.85;
torus.position.x = 1.7;
torus.position.y = 1;
torus.scale.x = 0.06;
torus.scale.y = 0.06;
torus.scale.z = 0.06;
torus.rotation.x = 89.8;
scene.add( torus );

const refTorGeometry = new THREE.TorusGeometry( 5, 0.4, 4, 18 );
const refTorMaterial = new THREE.PointsMaterial({
  size: 0.05,
  color: 0x7C9885
});
const refTorus = new THREE.Mesh( refTorGeometry, refTorMaterial );
refTorus.name = 'refTorus';
scene.add( refTorus );

// Create particles
const particlesGeometry = new THREE.BufferGeometry;
const particlesMaterial = new THREE.PointsMaterial({
  size: 0.05,
  color: 0xFC7753
});

// Create an array for the particles and place them on random places between 0 and 1
const particlesCnt = 256;
const posArray = new Float32Array(particlesCnt * 3);
for(let i = 0; i < particlesCnt * 3; i++) {
  posArray[i] = Math.random();
}

particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
const particlesMesh = new THREE.Points(particlesGeometry, particlesMaterial);

particlesMesh.position.x = 1.49;
particlesMesh.position.z = -0.6
particlesMesh.position.y = 0.74;
particlesMesh.scale.y = 0.001;
particlesMesh.scale.x = 0.71;
particlesMesh.scale.z = 0.8;
particlesMesh.rotation.x = 0.14;

scene.add(particlesMesh)

// Moves particles according to FFT, each particle gets their own frequency
function moveParts(freqArr) {
  if (isNaN(freqArr[0])) {} else {
    let positionAttribute = particlesMesh.geometry.attributes.position;
    for ( var i = 0; i < positionAttribute.count; i ++ ) {

      // access single vertex (x,y,z)
      var x = positionAttribute.getX( i );
      var y = positionAttribute.getY( i );
      var z = positionAttribute.getZ( i );

      // modify data (in this case just the z coordinate)
      z = Math.min(Math.max(-freqArr[i] * 50, -1), -0);

      // write data back to attribute
      positionAttribute.setXYZ( i, x, y, z );
      particlesMesh.geometry.attributes.position.needsUpdate = true;
    }
    // Keeps setting these variables because else it'll bug out
    particlesMesh.position.x = 1.49;
    particlesMesh.position.z = -0.6
    particlesMesh.position.y = 0.74;
    particlesMesh.scale.y = 0.001;
    particlesMesh.scale.x = 0.71;
    particlesMesh.scale.z = 0.8;
    particlesMesh.rotation.x = 0.14;
  }
}

function moveTorusParts(freqArr) {
  if (isNaN(freqArr[0])) {} else {
    let positionAttribute = torus.geometry.attributes.position;
    let refPositionAttribute = refTorus.geometry.attributes.position;
    for ( var i = 0; i < positionAttribute.count; i ++ ) {

      // access single vertex (x,y,z)
      var x = refPositionAttribute.getX( i );
      var y = refPositionAttribute.getY( i );
      var z = refPositionAttribute.getZ( i );

      // modify data (in this case just the z coordinate)
      z += Math.min(Math.max(freqArr[i] * 10, -80), 0);
      x += Math.min(Math.max(freqArr[i] * 10, -80), 0);

      // write data back to attribute
      positionAttribute.setXYZ( i, x, y, z );
      torus.geometry.attributes.position.needsUpdate = true;
    }
    // Keeps setting these variables because else it'll bug out
  }
}

// Interactie functies
function onDocumentMouseDown( event ) {
  event.preventDefault();

  readyMate = 1; // Only after this the particles will get moved, before this those receive -infinity and it'll bug out
  raycaster.setFromCamera( mouse, camera );

  // Check which part of the synth GLB object is clicked
  var intersects = raycaster.intersectObjects( scene.getObjectByName( "synth" ).children );
  var moveIntersect = raycaster.intersectObjects( scene.children );

  if ( intersects.length > 0 ) {
    if (intersects[0].object.name.includes('Key')) {

      // Get note from name of the key and plays it
      let pressNote = intersects[0].object.name.split('_');
      pressNote = pressNote[pressNote.length - 1];
      fmSynth1.triggerAttackRelease(pressNote, '8n');
      fmSynth2.triggerAttackRelease(pressNote, '8n');
      pluckSynth.triggerAttack(pressNote);

      // Rotates the key to appear pressed
      intersects[ 0 ].object.rotation.x = 0.1;
      oldkey = intersects[0].object;

    } else if (intersects[0].object.name.includes('rainCircle')) {  // Saves where you pressed the mouse and changes the variable to 1 to start changing the colour in onMouseMove

      heldMouse.x = ( event.clientX / window.innerWidth ) * 2 - 1;
    	heldMouse.y = - ( event.clientY / window.innerHeight ) * 2 + 1;
      changeColour = 1;
    } else if (intersects[0].object.name.includes('slideTriangle')) {   // Saves where you pressed the mouse and changes the variable to 1 to start changing the texture in onMouseMove

      slideTri = 1;
      heldMouse.x = ( event.clientX / window.innerWidth ) * 2 - 1;
    	heldMouse.y = - ( event.clientY / window.innerHeight ) * 2 + 1;

    }
  } else if ( moveIntersect.length > 0 ) {   // Check for the balls seperately because I made those in three.js

    moveableObject = moveIntersect[0].object;
    curBall = moveIntersect[0].object.name;
    isMoving = 1;
  }
}

// When releasing mouse resetting all values
function onDocumentMouseUp( event ) {
  event.preventDefault();
  if (typeof oldkey !== 'undefined') {
    oldkey.rotation.x = 0;
  }
  if (typeof isMoving !== 'undefined') {
    isMoving = 0;
  }
  if (typeof changeColour !== 'undefined') {
    changeColour = 0;
  }
  if (typeof slideTri !== 'undefined') {
    slideTri = 0;
  }
  if (typeof curBall !== 'undefined') {
    curBall = 0;
  }
}

function onMouseMove(event) {
  event.preventDefault();

  // Update mouse location
  mouse.x = ( event.clientX / window.innerWidth ) * 2 - 1;
	mouse.y = - ( event.clientY / window.innerHeight ) * 2 + 1;
  // Moves one of the balls to a location casted on the synth, limits the position to stay in the square

  if (isMoving == 1) {
    raycaster.setFromCamera( mouse, camera );
    var mIntersects = raycaster.intersectObjects(  scene.getObjectByName( "synth" ).children, true );
    if ( mIntersects.length > 0 ) {
        let xpos = Math.min(Math.max(mIntersects[0].point.x, -2.28), -1.5);
        let ypos = Math.min(Math.max(mIntersects[0].point.y, 0.56), 0.68);
        let zpos = Math.min(Math.max(mIntersects[0].point.z, -1.44), -0.59);
        moveableObject.position.x = xpos;
        moveableObject.position.y = ypos;
        moveableObject.position.z = zpos;
        // Change synth sounds for the first ball
        if (curBall.includes(1)) {
          // Scale harmonicity between 1 and 20.3
          fmSynth1.harmonicity.value = ((zpos + 1.44) * 10) + 1;
          fmSynth2.harmonicity.value = ((zpos + 1.44) * 10) + 1;
          // Scales between 0 and 1
          crossFade.fade.value = (xpos + 2.28) * 1.2820512;
        } else if (curBall.includes(2)) {
          // Scale detune between 14.21
          fmSynth1.detune.value = ((zpos + 1.44) * 10) + 1;

          // Scales between 200 and 2500
          pluckSynth.dampening = ((xpos + 2.28) * 5000) + 500;
        } else if (curBall.includes(3)) {
          // Scale chorus between ...
          chorus.depth = ((zpos + 1.44) * 30) + 1;
          chorus.frequency.value = ((zpos + 1.44) * 4) + 1;
          chorus.feedback.value = xpos + 2.28;
          // Scales between 200 and 2500
          fmSynth1.envelope.release = ((xpos + 2.28) * 500);
          fmSynth2.envelope.release = ((xpos + 2.28) * 500);
        }
    }

    // Changes the colour of the circle using x and y coordinates from the mouse
  } else if (changeColour == 1) {
      var mouseDistY = mouse.y - heldMouse.y;
      var mouseDistX = mouse.x - heldMouse.x;
      var newColour = getRainbow(mouseDistY, mouseDistX, .8, .8, .8, 0, 2, 4, 176, 79);
      scene.getObjectByName('rainCircle').material = new THREE.MeshBasicMaterial( { color: newColour } );
      // Sound changes
      freeverb.dampening = ((mouseDistY + 1) * 800) + 100;
      freeverb.roomSize.value = Math.min(Math.max((mouseDistX + 1) / 2., 0.), 1.);
      chorus.delayTime = (mouseDistX + 2) * 2;
      chorus.spread = Math.min(Math.max((mouseDistY + 1) / 2., 0.), 1.)

    // Moves the texture of the triangle according to the y coordinate of the mouse
  } else if (slideTri == 1) {
    console.log('kaas');
      var mouseDistY = mouse.y - heldMouse.y;
      scene.getObjectByName('slideTriangle').material.map.offset.y += mouseDistY;
      scene.getObjectByName('slideTriangle').material.map.offset.y = Math.min(Math.max(scene.getObjectByName('slideTriangle').material.map.offset.y, 0), 0.5);
      heldMouse.y = - ( event.clientY / window.innerHeight ) * 2 + 1;

      // All wishy washy math for the effect controls tweaked untill I liked the sound
      let tempRel1 = fmSynth1.modulationEnvelope.release;
      let tempAtt1 = fmSynth1.modulationEnvelope.attack;
      let tempModI = fmSynth1.modulationIndex.value;
      let tempDec = fmSynth1.modulationEnvelope.decay;
      let tempSus = fmSynth1.modulationEnvelope.sustain;
      let tempFilt = filter.frequency.value;

      tempModI += mouseDistY * 200.;
      fmSynth1.modulationIndex.value = Math.min(Math.max(tempModI, 0.), 1100.);
      fmSynth2.modulationIndex.value = Math.min(Math.max(tempModI, 0.), 1100.);

      tempRel1 += mouseDistY * 1000;
      fmSynth1.modulationEnvelope.release = Math.min(Math.max(tempRel1, 50), 900);
      fmSynth2.modulationEnvelope.release = Math.min(Math.max(tempRel1, 50), 900);

      tempAtt1 += -mouseDistY * 50;
      fmSynth1.modulationEnvelope.attack = Math.min(Math.max(tempAtt1, 10), 100);
      fmSynth2.modulationEnvelope.attack = Math.min(Math.max(tempAtt1, 10), 100);

      tempDec += -mouseDistY * 50;
      fmSynth1.modulationEnvelope.decay = Math.min(Math.max(tempDec, 50), 200);
      fmSynth2.modulationEnvelope.decay = Math.min(Math.max(tempDec, 50), 200);

      tempSus += -mouseDistY;
      fmSynth1.modulationEnvelope.sustain = Math.min(Math.max(tempSus, 0.5), 1);
      fmSynth2.modulationEnvelope.sustain = Math.min(Math.max(tempSus, 0.5), 1);

      tempFilt += mouseDistY * 10000;
      filter.frequency.value = Math.min(Math.max(tempFilt, 1000), 19000);

    }
  }

// Check for mouse events
document.addEventListener( 'mousedown', onDocumentMouseDown );
document.addEventListener( 'mouseup', onDocumentMouseUp );
document.addEventListener('mousemove', onMouseMove);

// Render the scene
function animate() {
  torus.scale.x = meter1.getValue() / 2;
  torus.scale.y = meter2.getValue() / 2;

  // Move particles
  var freqs = toneFFT.getValue(0);
  moveParts(freqs);

  // Change particles colour
  var newPartColour = getRainbow(freqs[240] * 100000,freqs[240] * 100000, .8, .8, .8, 0, 2, 4, 176, 79);
  particlesMesh.material = new THREE.PointsMaterial({
    size: 0.05,
    color: newPartColour
  });

  // Change torus colour
  var waveformArray = toneWaveform.getValue();
  var newTorusColour = getRainbow(waveformArray[0] * 1000,waveformArray[0] * 1000, .8, .8, .8, 0, 2, 4, 176, 79);
  torus.material = new THREE.PointsMaterial({
    size: 0.05,
    color: newTorusColour
  });

  // Distort Torus
  moveTorusParts(waveformArray);

	requestAnimationFrame( animate );
	renderer.render( scene, camera );

}


animate();
