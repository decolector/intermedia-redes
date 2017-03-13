/*
Introducción al dibujo en processing.
Usando primitivos gráficos y estructuras de control básicas
es posible realizar composiciones abstractas estáticas.
Camilo Martinez. 2015
cmart@decolector.net
*/
size(960, 540);
smooth();
//}


background(255);


// Hilera de cuadrados
fill(0);
noStroke();
for(int i = 0; i < 96 ; i++){
  rect( i*10, height/2, 8, 8);
}

/*
//fibonacci for loop

int f0 = 0;
int f1 = 1;
int f2 = 1;

for (int i = 0; i < 20;  i++) {
  f0 = f1;
  f1 = f2;
  f2 = f0 + f1;
  println(f2);//shows chars
  rect( 0, i*10, f2, 8);
  
  }
*/

/*
//Columnas de colores
noStroke();
for(int i = 0; i < 96 ; i++){
  fill(i*2.3);
  rect( i*10, 0, 10, height);
}
*/

/*
//Cuadrícula de cuadrados
for(int i = 0; i < 96 ; i++){
  for (int j = 0; j < 54; j++){
    rect( i*10, j*10, 8, 8);
  }
}
*/


/*
noFill();
stroke(0);
for ( int i = 0; i < 100; i++){
  float x1 = random(0, width);
  float y1 = random(0, height);
  float x2 = random(0, width);
  float y2 = random(0, height);

  line( x1, y1, x2, y2);
}
*/


/*
//Distribución gausiana
noFill();
stroke(0);
for ( int i = 0; i < 100; i++){
  float x1 = randomGaussian() * width/2;
  float y1 = randomGaussian() * height/2;
  float x2 = randomGaussian() * width/2;
  float y2 = randomGaussian() * height/2;

  line( x1, y1, x2, y2);
}

*/

/*
//Distribución gausiana, variación
noFill();
stroke(0);

int divisor1 = 4;
int divisor2 = 2;
for ( int i = 0; i < 100; i++){
  float x1 = (randomGaussian() * width/divisor1) + width/divisor2;
  float y1 = (randomGaussian() * height/divisor1)+ height/divisor2;
  float x2 = (randomGaussian() * width/divisor1) + width/divisor2;
  float y2 = (randomGaussian() * height/divisor1) + height/divisor2;

  line( x1, y1, x2, y2);
}
*/

/*
//Polar a Cartesiano
float radio = 260;

for(int i = 0; i < 360; i += 10){
  float angulo = float(i);
  pushMatrix();
  translate(width/2, height/2);
  println(angulo);
  float x = sin(radians(angulo)) * radio;
  float y = cos(radians(angulo)) * radio;
  line(0,0,x,y);
  popMatrix();
}
*/