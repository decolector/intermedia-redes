/*
//Programa que busca en el api de tumblr post con imagenes y las muestra en el canvas
//Usa la librería temboo y el api de tumblr
// Camilo Martinez ( cmart@decolector.net )
// Noviembre 2015
*/

import com.temboo.core.*;
import com.temboo.Library.Tumblr.Tagged.*;

JSONObject res;

PImage[] images = new PImage[0];

// Create a session using your Temboo account application details
TembooSession session = new TembooSession("decolector", "tumblrbot", "cPmpyneBRhdxtgdlRQWN4QSaMjArujr2");

void setup() {
  size(800, 600);
  // Run the RetrievePostsWithTag Choreo function
  runRetrievePostsWithTagChoreo();
}

void runRetrievePostsWithTagChoreo() {
  // Create the Choreo object using your Temboo session
  RetrievePostsWithTag retrievePostsWithTagChoreo = new RetrievePostsWithTag(session);

  // Configurando la busqueda en tumblr, 
  //aca es necesario el oauth secret o api key que entrega tumblr cuando registramos la aplicacion. 
  retrievePostsWithTagChoreo.setAPIKey("zayqyCTYWihbq4lVYcG53E6LeQf7l5rp4EC04g7l1Z6OAva5hC");
  retrievePostsWithTagChoreo.setTag("cats");

  // Run the Choreo and store the results
  RetrievePostsWithTagResultSet retrievePostsWithTagResults = retrievePostsWithTagChoreo.run();
  
  // Print results
  //println(retrievePostsWithTagResults.getResponse());
  
  res = parseJSONObject(retrievePostsWithTagResults.getResponse());
  //procesamos la respuesta del servidor
  processResponse(res);
}

void processResponse(JSONObject res){
  //extraemos el array JSON que cotiene info sobre los posts
  JSONArray resarray = res.getJSONArray("response");
  
  //iteramos por el objeto
  for(int i = 0; i < resarray.size(); i++){
    JSONObject obj = resarray.getJSONObject(i);
    
    //verificamos si existe un post con fotos
    if(obj.hasKey("photos")){
      JSONArray parray = obj.getJSONArray("photos");
      //extraemos la url de la imagen  
      String url = parray.getJSONObject(0).getJSONObject("original_size").getString("url");
      println(url);
      PImage img = loadImage(url);
      //Guardamos la imagen en la lista de imagenes a mostrar
      images = (PImage[])append(images, img);
    }
  }
}

void draw(){
  //iteramos por el array que contiene las imagenes 
  for(int i = 0; i < images.length; i++){
    image(images[i], 0, i*100);
  }
}