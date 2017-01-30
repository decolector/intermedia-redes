
size(600, 900);
background(255);
strokeWeight(2);
smooth();

//variable para guardar el numero de lineas a generar
int numlines = 75;

// variables para guardar el ultimo punto generado
float px = random(width);
float py = random(height);

////// version básica
/*
//variable para determinar si la linea es vertical u horizontal
int vertical = 0;

for(int i = 0; i < numlines; i++){
  if(vertical == 0){
    float x1 = px;
    float y1 = py;
    float x2 = x1;
    float y2 = random(height);
    line(x1, y1, x2, y2);
    px = x2;
    py = y2;
    //cambiamos el contador a 1 para dibujar una linea verical en la siguiente iteracion

    vertical = 1;
  }else{
    float x1 = px;
    float y1 = py;
    float x2 = random(width);
    float y2 = y1;
    line(x1, y1, x2, y2);
    px = x2;
    py = y2;
    vertical = 0;
  }
}
*/


//// version optimizada.

for(int i = 0; i < numlines; i++){
  // con esta operacion sabemos si i es par o impar
  if(i % 2 == 0){ 
    //el punto inicial de la linea actual
    //es el mismo punto final de la linea pasada
    float x1 = px;
    float y1 = py;
    
    //como la linea es horizontal x1 y x2 son iguales
    float x2 = x1;
    
    //y2 lo generamos aleatoriamente
    float y2 = random(height);
    
    //dibujamos la línea
    line(x1, y1, x2, y2);
    
    //guardamos el ultimo punto de la linea en las variables
    //para usarlas en la proxima linea
    px = x2;
    py = y2;
    
  }else{ //si i es impar, dibujamos linea vertical
  
    //el punto inicial de la linea actual
    //es el mismo punto final de la linea pasada
    float x1 = px;
    float y1 = py;
    
    //como la linea es vertical y1 y y2 valen lo mismo
    float y2 = y1;
    
    //x2 lo generamos aleatoriamente
    float x2 = random(width);
    
    //dibujamos la linea
    line(x1, y1, x2, y2);
    
    //guardamos el ultimo punto de la linea en las variables
    //para usarlas en la proxima linea    
    px = x2;
    py = y2;

  }
}
