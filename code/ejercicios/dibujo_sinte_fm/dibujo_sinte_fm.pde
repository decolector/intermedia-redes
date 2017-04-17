
//importacion de la libreria de sonido
import ddf.minim.*;
import ddf.minim.ugens.*;

//variable que contendra la libreria y todas sus funciones
Minim minim; 
//variable que representa la salida de audio
AudioOutput out;
//variable para el osilador
Oscil onda;
Oscil fm;

Frequency freq;

void setup(){
  size(800, 600);
  background(255);
  minim = new Minim(this);//inicializacion de la libreria
  out = minim.getLineOut();//inicializacion de la salida
  onda = new Oscil(200, 0.8f, Waves.TRIANGLE);//creación del osilador
  fm   = new Oscil( 10, 2, Waves.SINE );
  fm.offset.setLastValue( 200 );  
  fm.patch( onda.frequency );
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

  //dos variables resultantes de mapear mouseX y mouseY

  float modulateAmount = map( mouseY, 0, height, 220, 1 );
  float modulateFrequency = map( mouseX, 0, width, 0.1, 100 );
  
  //aqui son usadas como frecuencia y amplitud de al onda fm  
  fm.setFrequency( modulateFrequency );
  fm.setAmplitude( modulateAmount );
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