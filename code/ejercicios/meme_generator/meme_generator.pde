/*
  Este programa genera memes usando imágenes populares de memes
  y citas famosas de Michel Foucault
*/

//variable para la imagen de fondo
PImage fondo; 
//variable para la fuente
PFont impact;
//lista de nombres de archivos de imagen
String[] filenames = {
  "alone.png",
  "doge.png",
  "feel_like_a_sir.jpg",
  "grumpy.png",
  "lol.jpg",
  "troll.png",
  "success.png",
  "rage.png",
  "yuno.png",
  "feels.png"
};
//lista para las imagenes
//esta lista inicia con el mismo numero de nombres de archivo

PImage[] images = new PImage[filenames.length];

//imagen principal
PImage img;

//las siguientes son citas de Michel Foucault, divididas en dos
// y repartidas en dos listas

//lista primera parte de frases
String[] frasesA = {
  "Donde hay poder,",
  "Lo propio del saber",
  "Estoy feliz con mi vida",
  "Hay que ser un héroe",
  "El saber es el único",
  "El individuo es",
  "Lo que quiero comunicar"
};
//lista de segunda parte de frases
String[] frasesB = {
  "Hay resistencia",
  "no es ni ver ni demostrar, \nsino interpretar",
  "pero no tanto conmigo mismo",
  "para enfrentarse \na la moralidad de la época",
  "espacio de libertad del ser",
  "el producto del poder",
  "no es que todo es malo,\nsino que todo es peligroso" 
};
//variables para seleccionar las partes de una frase
String fraseA, fraseB;

void setup(){
  size(600, 600);
  impact = loadFont("Impact-48.vlw");//cargamos la fuente
  textFont(impact);//seleccionamos la fuente para el texto
  textAlign(CENTER);//texto centrado
  fondo = loadImage("back00.jpg");//cargamos la imagen de fondo
  background(fondo);//dibujamos la imagen en el fondo
  stroke(255);
  fill(0);
  //iteramos por la lista de nombres de archivos de imagen

  for( int i = 0; i < filenames.length; i++ ){
  //por cada archivo, cargamos el archivo correspondiente en
  //la lista de imagenes
    images[i] = loadImage(filenames[i]);
  }
  //un numero entero aleatorio entre 0 y el numero de imagenes
  int rand_img = int(random(images.length));
  //seleccionamos la imagen correspondiente de la lista usando el numero aleatorio
  img = images[rand_img];
  //un numero aleatorio entre 0  y el numero de frases en la lista
  int rand_frase = int(random(frasesA.length));
  //cargamos la primera y segunda parte de la frase usando el numero aleatorio
  fraseA = frasesA[rand_frase];
  fraseB = frasesB[rand_frase];
}

void draw(){
  background(fondo);//dibujamos el fondo siempre
  image(img, 0, 0, 600, 600);//dibujamos la imagen principal
  
  //lo siguiente son las rutinas de formato y ubicacion del texto
  textSize(50);
  fill(255);
  text(fraseA, (width/2) + 2, 52);
  fill(0);
  text(fraseA, width/2, 50);
  fill(255);
  textSize(42);
  text(fraseB, (width/2) + 2, 502);
  fill(0);
  text(fraseB, width/2, 500);

}
//cada vez que el usuario hace click
void mouseClicked(){
  //cargamos una nueva imagen y una nueva frase por partes.
  int rand_img = int(random(images.length));
  img = images[rand_img];
  int rand_frase = int(random(frasesA.length));
  fraseA = frasesA[rand_frase];
  fraseB = frasesB[rand_frase];
}

//si el usuario presiona una tecla 
void keyPressed(){
  //y la tecla es la g
  if(key == 'g'){
    //guardamos la imagen actual de la ventana
    saveFrame("meme-###.png");
  }
}