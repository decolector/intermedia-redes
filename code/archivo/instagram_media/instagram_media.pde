import com.temboo.core.*;
import com.temboo.Library.Instagram.*;

//Iniciamos sesion con Temboo
TembooSession session = new TembooSession("account", "app", "key");

//Array de imagenes para renderizar
PImage[] images = new PImage[0];

//Contador de minutos
int min = 0;


//Setup
void setup() {
  size(1024, 306);
  
  //min es igual al minuto actual 
  min = minute();
  //Hacemos una primera busqueda en instagram
  runSearchMediaChoreo();
}


//Funcion de dibujo
void draw(){
  
  background(0);
  
  //Si hay imagenes en el array, las mostramos
  for(int i = 0; i < images.length; i++){
    //La posicion de las imagenes respecto al X del mouse
    float posx = map(mouseX, 0, width, 0, 306);
    //renderizamos la imagen correspondiente
    image(images[i], i*posx, 0.0, 306, 306); 
  }
  
  //Si ha pasado un minuto
  if(min != minute()){
    min = minute();
    println("one min passed: (" + min + " )");
    runSearchMediaChoreo();
  }
}


//Funcion de busqueda: Se encarga de buscar las imagenes en instagram y entregar los resultados
void runSearchMediaChoreo() {
  // Creamos el objeto choreo usando la sesion de Temboo;
  SearchMedia searchMediaChoreo = new SearchMedia(session);

  // Set inputs
  searchMediaChoreo.setClientID("client_id");
  searchMediaChoreo.setLatitude("40.7128");
  searchMediaChoreo.setLongitude("74.0059");
  // Configuramos las opciones de busqueda

  //Bogota lat long
  //searchMediaChoreo.setLatitude("4.5981");
  //searchMediaChoreo.setLongitude("74.0758");

  // Ejecutamos el choreo y guardamos los resltados en la variable
  SearchMediaResultSet searchMediaResults = searchMediaChoreo.run();
  JSONObject res = parseJSONObject(searchMediaResults.getResponse());
  
  //Pasamos la variable a la funcion de parseo
  parseResponse(res);

}

//////////////////////////////
//Funcion de parseo: se encarga de descomponer el objeto y sacar las imagenes
void parseResponse(JSONObject response){
  println("Obteniendo respuesta");
  //println(response);
  //Sacamos el array de resultados
  JSONArray data = response.getJSONArray("data");
  
  //Y lo procesamos
  for(int i = 0; i < data.size(); i++){
    //Extraemos el objeto que representa un resultado
    JSONObject obj = data.getJSONObject(i);
    
    //Y extraemos el tipo de media
    String type = obj.getString("type");
    println("Media type: " + type);
    
    //Si el tipo de media es imagen
    if( type.equals("image")){
      //Extraemos el obj imagenes
      JSONObject imgs = obj.getJSONObject("images");
      //Luego el la imagen de baja resolucion
      JSONObject low = imgs.getJSONObject("low_resolution");  
      //Luego la url
      String url_str = low.getString("url");
      //en la url que llega nos sobra lo que va despues del '?', esta línea recorta esa parte
      String url = split(url_str, '?')[0];
      //println(url);
      //Cargamos la imagen con la url
      PImage img = loadImage(url);
      //Guardamos la imagen en la lista de imagenes a mostrar
      images = (PImage[])append(images, img);
    }
  }
}