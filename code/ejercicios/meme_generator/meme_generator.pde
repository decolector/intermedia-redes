


PImage img;
PImage back;

void setup(){
  size(600, 600);
  background(255);
  img = loadImage("yuno.png");
  fill(255,0,0);
}

void draw(){
  image(img, 0, 0, 600, 600);
  textSize(48);
  text("computador", 200, 50);
  textSize(32);
  text("porqué nunca haces lo que te digo ?", 30, 500);
}