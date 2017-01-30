

/*
* Movimiento lineal con rebote ( usando vectores )
* En mecánica, el movimiento es un cambio de la posición de un cuerpo  
* a lo largo del tiempo respecto de un sistema de referencia[1].
* [1]: https://en.wikipedia.org/wiki/Linear_motion
**/

int rad = 25; //radio del elipse
int velx = 1; //velocidad en x
int vely = 1; //velocidad en y 

float posx = 0; //posición en x
float posy = 0; //posición en y



void setup(){
  size(800,600); 
  //inicializamos las posiciones en la mitad del espcio
  posx = width/2;
  posy = height/2;
  
  //la velocidad de actualizacion del sistema
  frameRate(30);
  
  //Algunas configuraciones de apariencia
  noSmooth();
  noStroke();
  fill(0);
}

void draw(){
  
  //actualizamos la posicion del objeto
  posx = posx + velx;
  posy = posy + vely;
  
  
  //Verificamos que la posicion esté dentro de los limites
  //del espacio, 
  if(posx > width-rad || posx < 0 + rad){
    
    //si el objeto se encuentra por fuera, invertimos su direccion.
    velx *= -1;
  }
  
  //lo mismo para la posicion en y
  if(posy > height-rad || posy < 0 + rad){
    vely *= -1;
  }
  
  //verificamos en la terminal los datos
  println("posx: " + posx + ", posy: " + posy);
  
  background(255);
  
  //se dibuja el elipse en la posicion actualizada
  ellipse(posx, posy, rad*2, rad*2);
}


//Interaccion con el teclado

void keyPressed(){
  //Al presionar la tecla 's'...
  if(key == 's'){
    //.. aumentamos la velocidad segun la direccion del movimiento

    if(velx > 0 ){
      velx++;
    }else{
      velx--;
    }
  }
  
  //Al presionar la tecla 'a'
  if(key == 'a'){
  //...aumentamos la velocidad en y
    if(vely > 0){
      vely++;
    }else{
      vely--;
    }
  }
  
   if(key == 'q'){
    //.. aumentamos la velocidad segun la direccion del movimiento

    if(velx < 0 ){
      velx--;
    }else{
      velx++;
    }
  }
  
  //Al presionar la tecla 'a'
  if(key == 'w'){
  //...aumentamos la velocidad en y
    if(vely > 0){
      vely--;
    }else{
      vely++;
    }

  }
}
