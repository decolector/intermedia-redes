Particula part;
 
void setup() {
  size(640,360);
//Creamos la partícula
  part = new Particula();
}
 
void draw() {
  background(255);
 
//Funciones o capacidades del objeto Particula.
  part.actualizar();
  part.comprobarLimites();
  part.dibujar();
}



//Aqui se define lo que es y puede hacer una particula (Clase)
class Particula {
 
//El objeto posee dos propiedades o variables de tipo PVector: posicion and velocidad.
  PVector posicion;
  PVector velocidad;
  
  int radio;
 
  Particula() {
    posicion = new PVector(random(width),random(height));
    velocidad = new PVector(random(-2,2),random(-2,2));
    radio = 25;
  }
 
  void actualizar() {
//La posicion cambia al aplicar velocidad
    posicion.add(velocidad);
  }
 
  void dibujar() {
    stroke(0);
    fill(175);
    ellipse(posicion.x,posicion.y, radio, radio);
  }
 
 //Esta funcion comprueba que la posicion del objeto este dentro de los limites
 //del espacio, creando un espacio toroidal
 /*
  void comprobarLimites() {
    if (posicion.x > width) {
      posicion.x = 0;
    } else if (posicion.x < 0) {
      posicion.x = width;
    }
 
    if (posicion.y > height) {
      posicion.y = 0;
    } else if (posicion.y < 0) {
      posicion.y = height;
    }
  } 
  */
  
   //Esta funcion comprueba que la posicion del objeto este dentro de los limites
 //del espacio, creando un espacio toroidal
 
  void comprobarLimites() {
    //Verificamos que la posicion esté dentro de los limites
    //del espacio, usando los componentes individuales de cada vector.
    if ((posicion.x > width - radio) || (posicion.x < 0 + radio)) {
      //si el objeto se encuentra por fuera, invertimos su direccion.
      velocidad.x = velocidad.x * -1;
    }
    if ((posicion.y > height - radio) || (posicion.y < 0 + radio)) { 
      //si el objeto se encuentra por fuera, invertimos su direccion.
      velocidad.y = velocidad.y * -1;
    }
  } 
  
}
