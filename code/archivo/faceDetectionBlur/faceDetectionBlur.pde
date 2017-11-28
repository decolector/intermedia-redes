/*
Este programa detecta un rostro humano y aplica un filtro BLUR sobre el rostro detectado
Usa la librería openCV y el haar cascade "FRONTALFACE"

Escrito por Camilo Martinez, basado en el ejempo original de Greg Borenstein
*/

import gab.opencv.*;
import processing.video.*;
import java.awt.*;
import java.awt.Rectangle;

OpenCV opencv;
//lista para guardar los rectangulos que contienen rostros
Rectangle[] faces;
Capture video;

void setup() {
  size(640, 480);
  video = new Capture(this, width, height); //objeto de captura de video
  opencv = new OpenCV(this, width, height);//objeto de visión artificial
  
   // este es el haar cascade conteniendo la definicion de un rostro
  opencv.loadCascade(OpenCV.CASCADE_FRONTALFACE);//  
  video.start();
}

void draw() {
  opencv.loadImage(video);//cargar la imagen de video en opencv para poder analizarla.
  
  //detecta los rostros y los guarda en la lista faces
  //un face en realidad es un cuadrado que encierra el rostro detectado
  faces = opencv.detect();
  
  image(video, 0, 0 );//dibujamos la imagen del video

  noFill();
  stroke(0, 255, 0);
  strokeWeight(3);
  //por cada por cada rostro detectado, dibujamos el rectangulo que lo encierra
  for (int i = 0; i < faces.length; i++) {
    //aqui usamos los datos asignados a cada rostro para graficarlo sobre la pantalla
    //rect(faces[i].x, faces[i].y, faces[i].width, faces[i].height);
    
    //creamos una imagen vacía por cada rostro detectada
    PImage censor = createImage(faces[i].width, faces[i].height, RGB);
    //copiamos la region correspondiente al rostro de la imagen del video a la imagen vacia
    censor.copy(video, faces[i].x, faces[i].y, faces[i].width, faces[i].height, 0, 0, censor.width, censor.height);
    //aplicamos el filtro blur a la imagen
    censor.filter(BLUR, 6);
    //dibujamos la imagen en el lugar del rostro
    image(censor, faces[i].x, faces[i].y, faces[i].width, faces[i].height);
  }
}


//evento de captura de video, este es necesario para que el sketch funcione.
void captureEvent(Capture c) {
  c.read();
}