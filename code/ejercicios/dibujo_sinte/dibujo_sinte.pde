
//importacion de la libreria de sonido
import ddf.minim.*;
import ddf.minim.ugens.*;

//variable que contendra la libreria y todas sus funciones
Minim minim; 
//variable que representa la salida de audio
AudioOutput out;
//variable para el osilador
Oscil onda;

Frequency freq;

void setup(){
  size(800, 600);
  background(255);
  minim = new Minim(this);//inicializacion de la libreria
  out = minim.getLineOut();//inicializacion de la salida
  freq = Frequency.ofPitch("A4");//iniciamos con una frecuenca de 440hz
  onda = new Oscil(freq, 0.6f, Waves.TRIANGLE);//creación del osilador
  onda.patch(out);//conectamos el oscilador a la salida de audio para que suene
}
//en el draw no pasa nada
void draw(){

}

//todo pasa cuando el usuario arrastra el mouse
void mouseDragged(){
  //distancia entre el la posicion actual y pasada del mouse
  float d = dist(mouseX, mouseY, pmouseX,pmouseY);
  //mapeo de la distancia a valores de grosor de linea
  float s = map(d, 0, 500, 0, 100);
  //mapeos de posicion del mouse a color
  float r = map(mouseX, 0, width, 0, 255);
  float g = map(mouseY, 0, height, 0, 255);
  float b = 128;
  //usamos las variables anteriores para crear un color
  color relleno = color(r,g,b);
  //usamos ese color como relleno
  stroke(relleno);
  //usamos s como grosor de borde
  strokeWeight(s);
  //dibujamos la línea
  line(mouseX, mouseY, pmouseX, pmouseY);
  
  //mapeo de posicion X del mouse a un rango de frecuencias
  //tomado de aqui: http://www.phy.mtu.edu/~suits/notefreqs.html
  float fx = map(mouseX, 0, width, 16.351, 15804.264);
  //usamos el resultado como frecuencia en Hertz
  freq.setAsHz(fx);
  //asignamos la frecuencia a la onda
  onda.setFrequency(freq);
}

void keyPressed(){
  //si se presiona b, borramos
  if(key == 'b'){
    background(255);
  }
  //si se presiona g, guardamos la imagen actual.
  if(key == 'g'){
    saveFrame("dibujo-###.png");
    println("Nuevo archivo guardado.");
  }
}