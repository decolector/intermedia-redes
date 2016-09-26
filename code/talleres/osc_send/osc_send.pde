import oscP5.*;
import netP5.*;

OscP5 oscP5;
NetAddress myRemoteLocation;

int on = 255;
int off = 0;
String msg = "";

void setup(){
  size(512, 256);
  oscP5 = new OscP5(this, 12000);
  myRemoteLocation = new NetAddress("127.0.0.1", 12000);
  textSize(24);
}

void draw()
{
  background(0);
  stroke(255);
  if (mousePressed) {
    if (mouseX<width/2) {
      fill(on);
      rect(0, 0, width/2, height);
      fill(off);
      text("SNARE", width/4, height/2);
    } else {
      fill(on);
      rect(width/2, 0, width, height);
      fill(off);
      text("KICK", (width/4)*3, height/2);
    }
  } else {
    fill(on);
    text("CLICK", width/2, height/2);
  }
}

void mousePressed() {
  if (mouseX<width/2) {
    sendSnare();
  } else {
    sendKick();
  }
}

void keyPressed() 
{
  if ( key == 's' ) {
    sendSnare();
  }

  if ( key == 'k' ) {
    sendKick();
  }
}
void sendSnare() {
  /* in the following different ways of creating osc messages are shown by example */
  msg = "snare";
  OscMessage myMessage = new OscMessage("/snare");
  myMessage.add(msg); /* add an int to the osc message */
  /* send the message */
  oscP5.send(myMessage, myRemoteLocation);
  
}

void sendKick() {
  msg = "kick";
  OscMessage myMessage = new OscMessage("/kick");
  myMessage.add(msg); /* add an int to the osc message */
  /* send the message */
  oscP5.send(myMessage, myRemoteLocation);
}