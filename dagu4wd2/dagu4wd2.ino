int motor1[4] = {4,5, 6, 7}; //  order 0 - gnd, 1- dir( 0 forwad, 1 - back), 2 - pwm, 3 - brk  (1 to halt)
int motor2[4] = {8,9,10,11}; // common halt for the time being


void setup()
{

Serial.begin(9600);
Serial.println("Program Startted");

  for(int i=0;i<4;i++){
    pinMode(motor1[i], OUTPUT);
    pinMode(motor2[i], OUTPUT);
    digitalWrite(motor1[i], 0);
    digitalWrite(motor2[i], 0);
    // integrating both the motors
  }
  Serial.setTimeout(20);
}

void forward(int analogl = 255, int analogr =255 ){


digitalWrite(motor1[1],0 );
analogWrite(motor1[2], analogl);

digitalWrite(motor2[1],0 );
analogWrite(motor2[2], analogr);
digitalWrite(motor1[3], 0 );
digitalWrite(motor2[3], 0 );
//delay(50);
}

void back(int analogl = 255, int analogr =255){

digitalWrite(motor1[1],1 );
analogWrite(motor1[2],analogl);

digitalWrite(motor2[1],1 );
analogWrite(motor2[2], analogr);
digitalWrite(motor1[3], 0 );
digitalWrite(motor2[3], 0 );

//delay(50);

}

void left(int analogl = 255, int analogr =255){
  
digitalWrite(motor1[1],1 );
analogWrite(motor1[2],analogl);

digitalWrite(motor2[1],0 );
analogWrite(motor2[2], analogr);
digitalWrite(motor1[3], 0 );
digitalWrite(motor2[3], 0 );

//delay(50);
}

void right(int analogl = 255, int analogr =255){
  
digitalWrite(motor1[1],0 );
analogWrite(motor1[2],analogl);

digitalWrite(motor2[1],1 );
analogWrite(motor2[2], analogr);
digitalWrite(motor1[3], 0 );
digitalWrite(motor2[3], 0 );

//delay(50);
}
void stopm(){


digitalWrite(motor2[3], 1 );

digitalWrite(motor1[3], 1 );
//delay(50);
}




void loop(){
	if(Serial.available() !=0){
	 
		String val = Serial.readString();
    //Serial.println(val[0]);
    //Serial.println((int)val[1]); //  analogl
    //Serial.println((int)val[2]); // analogr
   
    
		switch(val[0]){
		case 'x' :Serial.println("Stopped");
		stopm();
      
			break;
		case 'w': Serial.print("Forward Left Speed : "); Serial.print((int)val[1]);Serial.print(" Right Speed : "); Serial.println((int)val[2]); 
		forward((int)val[1],(int)val[2] );
    
			break;
		case 's': 
		 Serial.print("Back Left Speed : "); Serial.print((int)val[1]);Serial.print(" Right Speed : "); Serial.println((int)val[2]); 
		back((int)val[1],(int)val[2]);
   
   
			break;
      case 'a': 
    Serial.print("Left Left Speed : "); Serial.print((int)val[1]);Serial.print(" Right Speed : "); Serial.println((int)val[2]); 
    left((int)val[1],(int)val[2]);
   
   
      break;
      case 'd': 
     Serial.print("Right Left Speed : "); Serial.print((int)val[1]);Serial.print(" Right Speed : "); Serial.println((int)val[2]); 
    right((int)val[1],(int)val[2]);
   
   
      break;
      default : stopm();
      
	}
 Serial.flush();
//delay(1);

}


}

