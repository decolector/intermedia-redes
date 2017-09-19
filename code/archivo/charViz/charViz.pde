/*
*/

String texto = ""; //variable para guardar el texto
int posy; //posicion x del texto

void setup(){
  size(500,500);
  posy = 0;
  noStroke();
}

void draw(){
  background(0);
  
  
  for(int i = 0; i < texto.length(); i++){
    int c = int(texto.charAt(i));//encontramos el caracter, basado en el índice, lo convertimos a entero.
    float _f = constrain(c, 32,126); //limitamos los valores para que entren en el rango 32 a 126
    float f = map(_f, 32, 126, 0, 255); //mapeamos el valor a al rango 0,255.
    fill(f);//usamos el nuevo valor como color de relleno
    int posx = (i*10) % width;//formula para hallar posicion en x basado en el indice.
    posy = ((i*10) / width)*10;//lo mismo para y
    println(posy);
    rect(posx, posy, 10, 10);//dibujamos el cuadrado en la posicion posx, posy.
  }
  //text(texto, 10, 10, width - 20, height - 20);//dibujamos el texto encima de todo

}

void keyPressed(){
  if(key ==  BACKSPACE){
    texto = texto.substring(0, texto.length() - 1);
  }else{
    texto += key; //al presionar cualquier tecla, agregamos el caracter a la variable texto.
  //println(int(key));//imprimimos el numero que representa la letra.
  }
}