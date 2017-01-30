import http.requests.*;
import gifAnimation.*;


PImage[] gifs;

public void setup() 
{
	size(400,400);
	smooth();
  GetRequest get = new GetRequest("http://api.giphy.com/v1/gifs/search?q=funny+cat&api_key=dc6zaTOxFJmzC");
  get.send(); // program will wait untill the request is completed
  println("response: " + get.getContent());
  gifs = new PImage[0];
  JSONObject response = parseJSONObject(get.getContent());
  JSONArray results = response.getJSONArray("data");
  println("imgs: ");
  for(int i=0;i< results.size();i++) {
    JSONObject result = results.getJSONObject(i);
    JSONObject imgs = result.getJSONObject("images");
    JSONObject img = imgs.getJSONObject("fixed_height");
    String url = img.getString("url");
    println(url);
    
    PImage resultgif = loadImage(url);
    //resultgif.loop();
    gifs = (PImage[])append(gifs, resultgif);
  }
  
}

void draw(){

  background(255);
  for(int i = 0; i < gifs.length; i++){
    image(gifs[i], i*100, i*100, 100, 100);
  }
}