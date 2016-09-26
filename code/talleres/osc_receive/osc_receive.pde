/**
 * oscP5sendreceive by andreas schlegel
 * example shows how to send and receive osc messages.
 * oscP5 website at http://www.sojamo.de/oscP5
 */
 
import oscP5.*;
import netP5.*;
import ddf.minim.*;

Minim minim;
AudioSample kick;
AudioSample snare;

int on = 255;
int off = 0;
String msg = "";

OscP5 oscP5;
NetAddress myRemoteLocation;

void setup() {
  size(256,512);
  /* start oscP5, listening for incoming messages at port 12000 */
  oscP5 = new OscP5(this,12000);
  minim = new Minim(this);
  
  
  // load BD.wav from the data folder
  kick = minim.loadSample( "BD.mp3", // filename
                            512      // buffer size
                         );
 if ( kick == null ) println("Didn't get kick!");
  
  // load SD.wav from the data folder
  snare = minim.loadSample("SD.wav", 512);
  if ( snare == null ) println("Didn't get snare!");
  textSize(24);
}


void draw() {
  background(0);
  println(msg);
  if(msg.equals("snare")){
    fill(on);
    rect(0,0,width,height/2);
    fill(off);
    text(msg, 20, height/4);
  }else if(msg.equals("kick")){
    fill(on);
    rect(0,height/2,width,height);
    fill(off);
    text(msg, 20, (height/4) * 3);
  }
}

void oscEvent(OscMessage theOscMessage) {
  /* check if theOscMessage has the address pattern we are looking for. */
  
  if(theOscMessage.checkAddrPattern("/snare")==true) {
    snare.trigger();
    println(msg);
    msg = theOscMessage.get(0).stringValue();
  } 
  if(theOscMessage.checkAddrPattern("/kick")==true) {
    kick.trigger();
}    
    msg = theOscMessage.get(0).stringValue();
    println(msg);

}