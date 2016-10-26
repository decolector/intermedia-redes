/*
Este programa detecta la parte superior de un cuerpo humano y dibuja un cuadrado resaltando el objeto detectado.
Usa la librería openCV y el haar cascade "UPPER_BODY"
*/

import gab.opencv.*;
import processing.video.*;
import java.awt.*;
import java.awt.Rectangle;

OpenCV opencv;
Rectangle[] bodies;
Capture video;

void setup() {
  size(640, 480);
  video = new Capture(this, width, height); //objeto de captura de video
  opencv = new OpenCV(this, width, height);//objeto de visión artificial
  
  // este es el haar cascade conteniendo la definicion de la parte superior del cuerpo humano
  opencv.loadCascade(OpenCV.CASCADE_UPPERBODY);  

   // este es el haar cascade conteniendo la definicion de un rostro
  //opencv.loadCascade(OpenCV.CASCADE_FRONTALFACE);//  
  video.start();
}

void draw() {
  opencv.loadImage(video);//cargar la imagen de video en opencv para poder analizarla.
  
  //detecta los cuerpos y los guarda en la lista bodies
  //un bodie en realidad es un cuadrado que encierra el cuerpo detectado
  bodies = opencv.detect();
  
  image(video, 0, 0 );//dibujamos la imagen del video

  noFill();
  stroke(0, 255, 0);
  strokeWeight(3);
  //por cada por cada cuerpo detectado, dibujamos el rectangulo que lo encierra
  for (int i = 0; i < bodies.length; i++) {
    //aqui usamos los datos asignados a cada bodie para graficarlo sobre la pantalla
    rect(bodies[i].x, bodies[i].y, bodies[i].width, bodies[i].height);
  }
  
}


//evento de captura de video, este es necesario para que el sketch funcione.
void captureEvent(Capture c) {
  c.read();
}