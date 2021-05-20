// init();
// async function init() {
//   const response = await fetch("a.out.wasm");
//   const buffer = await response.arrayBuffer();
//   const obj = await WebAssembly.instantiate(buffer);
//   functieNaam(obj);
// }

// function functieNaam(object) {


  function preload() {

  }


  let balArray = [];                            // Maakt een array voor cirkels
  let aantalcirkels= 2;                         // Geeft hoeveel cirkels er zijn
  var ballet;                                   // Bouwt een cirkel variabelen
  let x, y;                                     // Bouwt een x en y variabele
  let idnummer = 0;                             // Geeft elk variabele een nummer
  const WindowWidth  = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
  const WindowHeight = window.innerHeight|| document.documentElement.clientHeight|| document.body.clientHeight;
  let oldPixels;
  var foo = [];

  var blobs = [];


  class Blob {

    constructor(x, y) {
      this.x = x;
      this.y = y;
      let angle = random(0, 2 * PI);
      this.xspeed = random(2, 5) * Math.cos(angle);
      this.yspeed = random(2, 5) * Math.sin(angle);
      this.r = random(120, 240);
    }

    update() {
      this.x += this.xspeed;
      this.y += this.yspeed;
      if (this.x > width || this.x < 0) this.xspeed *= -1;
      if (this.y > height || this.y < 0) this.yspeed *= -1;
    }

    show() {
      noFill();
      stroke(0);
      strokeWeight(4);
      ellipse(this.x, this.y, this.r * 2, this.r * 2);
    }
  };

  function setup() {                            // Deze set alles up
    //let blobs = [];
    // let pink = color(255, 102, 204);
    // for(i = 0; i < 900 * 900 * 4; i += 4) {
    //   foo.push(red(pink));
    //   foo.push(green(pink));
    //   foo.push(blue(pink));
    //   foo.push(alpha(pink));
    // }
    createCanvas(1920, 1080);                     // Zorgt voor anti-aliasing
    for (i = 0; i < 10; i++) {
      blobs.push(new Blob(random(0, width), random(0, height)));
    }
  }

  // Manier om arrays goed geformat te krijgen voor c++ verkregen van https://medium.com/@tdeniffel/c-to-webassembly-pass-and-arrays-to-c-86e0cb0464f5
  function transferToHeap(arr) {
   heapSpace = Module._malloc(arr.length *
                       arr.BYTES_PER_ELEMENT); // 1
   Module.HEAP32.set(arr, heapSpace >> 2); // 2
   return heapSpace;
  }

  function getPxArr() {
    // Create arrays to pass to cpp
    let blobx = new Int32Array(10);
    let bloby = new Int32Array(10);
    let blobr = new Int32Array(10);

    // Populate cpp arrays
    for (i = 0; i< blobs.length; i++) {
      blobx[i] = Math.round(blobs[i].x);
      bloby[i] = Math.round(blobs[i].y);
      blobr[i] = Math.round(blobs[i].r);
    }
    let arrayOnHeapX;
    let arrayOnHeapY;
    let arrayOnHeapR;
    try {
       arrayOnHeapX = transferToHeap(blobx);
       arrayOnHeapY = transferToHeap(bloby);
       arrayOnHeapR = transferToHeap(blobr);
       // let pix =  Module.ccall('genGraph', // name of C function
       //  'number', // return type
       //  ['number','number','number','number','number','number'], // argument types
       //  [width, height, arrayOnHeapX, arrayOnHeapY, arrayOnHeapR, blobs.length()]); // arguments
       // ggenGraph = Module.cwrap('genGraph', 'number', ['number','number','number','number','number','number']);
       // let pix = ggenGraph(width, height, arrayOnHeapX, arrayOnHeapY, arrayOnHeapR, blobs.length());
       let pix = Module._ggenGraph(width, height, arrayOnHeapX, arrayOnHeapY, arrayOnHeapR, blobs.length);
       //console.log(Module._ggenGraph(w, h, arrayOnHeapX, arrayOnHeapY, arrayOnHeapR, le));
       console.log(pix);
       return pix;
     } catch (e) {
       error = e
     } finally {
       Module._free(arrayOnHeapX);
       Module._free(arrayOnHeapY);
       Module._free(arrayOnHeapR);
     }
  }

  function draw() {
    background(0);
    console.log("kaas");
    let arrayXOnHeap;
    let arrayYOnHeap;
    let arrayROnHeap;


    getPxArr();


    //result = Module.ccall("addNums", null, ["number", "number"], [buffer, arrayDataToPass.length])

    //Module._sum_up(arrayOnHeap, arr.length);


    loadPixels();
    // for (x = 0; x < width; x++) {
    //   for (y = 0; y < height; y++) {
    //     let sum = 255;
        // for (i = 0; i < blobs.length; i++) {
        //   let xdif = x - blobs[i].x;
        //   let ydif = y - blobs[i].y;
        //   let d = sqrt((xdif * xdif) + (ydif * ydif));
        //   sum += 4 * blobs[i].r / d;
        // }
    //     set(x, y, color(0, 0, sum));
    //   }
    // }

    // console.log(pix);
    updatePixels();



    for (i = 0; i < blobs.length; i++) {
      blobs[i].update();
    }
  }
// }
