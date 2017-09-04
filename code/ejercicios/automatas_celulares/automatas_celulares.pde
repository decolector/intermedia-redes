int[] cells = {0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };


int generation = 0;

int[] ruleset = {0,0,0,1,1,1,1,0}; 

void setup(){
  size(600, 600);
  background(255);

} 

void draw(){
  int[] newcells = new int[cells.length];

  for (int i = 1; i < cells.length-1; i++) {
    int left   = cells[i-1];
    int middle = cells[i];
    int right  = cells[i+1];
    int newstate = rules(left,middle,right);
    newcells[i] = newstate;
    
  }
  for(int i = 0; i<cells.length; i++){
    if(cells[i] == 1){
      fill(0);
    }else{
      fill(255);
    }
    rect(i * 10, generation * 10, 10, 10);
  }
  cells = newcells;
  generation++;
}

int rules (int a, int b, int c) {
  if      (a == 1 && b == 1 && c == 1) return ruleset[0];
  else if (a == 1 && b == 1 && c == 0) return ruleset[1];
  else if (a == 1 && b == 0 && c == 1) return ruleset[2];
  else if (a == 1 && b == 0 && c == 0) return ruleset[3];
  else if (a == 0 && b == 1 && c == 1) return ruleset[4];
  else if (a == 0 && b == 1 && c == 0) return ruleset[5];
  else if (a == 0 && b == 0 && c == 1) return ruleset[6];
  else if (a == 0 && b == 0 && c == 0) return ruleset[7];
  return 0;
}

int rulez (int a, int b, int c) {
  String s = "" + a + b + c;
  int index = Integer.parseInt(s,2);
  return ruleset[index];
}