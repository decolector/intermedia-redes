

//Listas de vectores para guardar las coordenadas de deformacion
PVector[] old_coords = new PVector[2];
PVector[] new_coords = new PVector[2];

//Creamos las coordenadas iniciales
old_coords[0] = new PVector(128, 256);
old_coords[1] = new PVector(384, 256);

//creamos las coordenadas nuevas
new_coords[0] = PVector.add(old_coords[0], new PVector(random(-100, 100), 0.0));
new_coords[1] = PVector.add(old_coords[1], new PVector(random(-100, 100), 0.0));

//Creamos la cadena de coordenadas para el comando 
String coords = str(int(old_coords[0].x)) 
  + "," + str(int(old_coords[0].y)) 
  + " " 
  + str(int(new_coords[0].x)) 
  + "," 
  + str(int(new_coords[0].y)) 
  + " " 
  + str(int(old_coords[1].x)) 
  + "," + str(int(old_coords[1].y)) 
  + " " + str(int(new_coords[1].x)) 
  + "," + str(int(new_coords[1].y)) ;
  
println(coords);

//Creamos el comando
String[] cmd = {
  "/usr/local/bin/convert", "data/sph.png", "-virtual-pixel", "Black", "-distort", "Shepards", coords, "data/output.png"
};
//String cmd = {"/usr/local/bin/convert data/sph.png -negate data/sphtiouiob.png";

//Este es el directorio desde donde se va a ejecutar el comando
//Adaptar esta linea al directorio actual donde esta el sketch
File wd = new File("/Users/cmart/javer/intermedia-redes/code/imagemagick/");

try {
  Process p = Runtime.getRuntime().exec(cmd, null, wd);
}
catch(Exception e) {
  println("Some error: ");
  println(e);
}


