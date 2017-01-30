

/*
* Movimiento lineal con rebote ( usando vectores )
* En mecánica, el movimiento es un cambio de la posición de un cuerpo  
* a lo largo del tiempo respecto de un sistema de referencia[1].
* [1]: https://en.wikipedia.org/wiki/Linear_motion
**/
int rad = 15; //radio del elipse
PVector posicion; //Posicion del cuerpo (x,y)
PVector velocidad; //Velocidad del cuerpo (vx, vy)
 
void setup() {
  size(640,360);
  posicion = new PVector(100,100);
  velocidad = new PVector(2.5,5);
  
  //Algunas configuraciones de apariencia
  noSmooth();
  noStroke();
  fill(0);
}
 
void draw() {
  background(255);
 //actualizamos la posicion del cuerpo agregando el vector velocidad
 //al vector de posicion
  posicion.add(velocidad);
  
  //Verificamos que la posicion esté dentro de los limites
  //del espacio, usando los componentes individuales de cada vector.
  if ((posicion.x > width - rad) || (posicion.x < 0 + rad)) {
    //si el objeto se encuentra por fuera, invertimos su direccion.
    velocidad.x = velocidad.x * -1;
  }
  if ((posicion.y > height - rad) || (posicion.y < 0 + rad)) {
    
    //si el objeto se encuentra por fuera, invertimos su direccion.
    velocidad.y = velocidad.y * -1;
  }
 
  background(255);
  //se dibuja el elipse en la posicion actualizada
  ellipse(posicion.x, posicion.y, rad*2, rad*2);
}

