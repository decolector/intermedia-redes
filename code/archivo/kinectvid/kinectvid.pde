// Daniel Shiffman
// Depth thresholding example

// https://github.com/shiffman/OpenKinect-for-Processing
// http://shiffman.net/p5/kinect/

// Original example by Elie Zananiri
// http://www.silentlycrashing.net


//Este ejemplo usa la nube de puntos del kinect para saber si hay algun objeto frente al sensor.
//Usa dos variables para limitar el rango de detección. Al detectar algo, reproduce un video.
//Modificado por Camilo Martinez
//cmart@decolector.net

import org.openkinect.freenect.*;
import org.openkinect.processing.*;
import processing.video.*;

Movie movie;

Kinect kinect;

// Depth image
PImage depthImg;

// Which pixels do we care about?

//Este es el rango de deteccion
//Cambiar los valores cambia la distancia

int minDepth =  60;
int maxDepth = 460;


// What is the kinect's angle
float angle;

boolean presence = false;//presencia frente al kinect
boolean past_presence = false;//presencia frente al kinect en el instante pasado

boolean playing;//se esta reproduciendo la pelicula

void setup() {
  size(640, 480);

  kinect = new Kinect(this);
  kinect.initDepth();
  angle = kinect.getTilt();
  
  movie = new Movie(this, "lucky.mp4");//cargamos la pelicula


  // Blank image
  depthImg = new PImage(kinect.width, kinect.height);
  
  //movie.loop();//reproduccion del video en loop
}

void draw() {
  // Draw the raw image
  image(kinect.getDepthImage(), 0, 0);

  // Threshold the depth image
  int[] rawDepth = kinect.getRawDepth();
  
  int count = 0;//contador para saber si hay algo en el rango

  for (int i=0; i < rawDepth.length; i++) {
    if (rawDepth[i] >= minDepth && rawDepth[i] <= maxDepth) {
      depthImg.pixels[i] = color(255,0,0);
      count++;//por cada punto en el rango aumentamos el contador
    } else {
      depthImg.pixels[i] = color(0);
    }
  }
  
  //si el contador es mayor a cero, hay algo en el rango
  if(count > 0){
    presence = true;
  }else{
    presence = false;
  }

  //si hay algo ahora y algo en el instante anterior
  //es porque algo acabo de entrar (deteccion de bordes)
  if(presence && !past_presence){
    movie.loop();
    playing = true;
  }
  
  //si el objeto salio del rango, paramos el video
  if(!presence && past_presence){
    movie.stop();
    playing = false;
  }

  // Draw the thresholded image
  depthImg.updatePixels();
  image(depthImg, 96, 0, 96, 72);

  fill(0);
  text("TILT: " + angle, 10, 20);
  text("THRESHOLD: [" + minDepth + ", " + maxDepth + "]", 10, 36);
  
   if(playing){
     println("reproduciendo video ...");
     image(movie, 0, 0, width, height);
    }
    past_presence = presence;
}

// Adjust the angle and the depth threshold min and max
void keyPressed() {
  if (key == CODED) {
    if (keyCode == UP) {
      angle++;
    } else if (keyCode == DOWN) {
      angle--;
    }
    angle = constrain(angle, 0, 30);
    kinect.setTilt(angle);
  } else if (key == 'a') {
    minDepth = constrain(minDepth+10, 0, maxDepth);
  } else if (key == 's') {
    minDepth = constrain(minDepth-10, 0, maxDepth);
  } else if (key == 'z') {
    maxDepth = constrain(maxDepth+10, minDepth, 2047);
  } else if (key =='x') {
    maxDepth = constrain(maxDepth-10, minDepth, 2047);
  }
}

void movieEvent(Movie m) {
  m.read();
}